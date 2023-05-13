import os
from notion_client import Client
import openai
from tqdm import tqdm


class NotionSummarizer:
    def __init__(self, database_name):
        """必要な情報のセッティングを行う

        Args:
            database_id (_type_): _description_
        """
        # Notion Integrationのトークンをセットする
        NOTION_API_KEY = '[Notion Integration Tokenに置き換えてください。]'
        token: str = os.environ.get("NOTION_TOKEN", NOTION_API_KEY)
        notion = Client(auth=token)
        self.notion = notion

        # OpenAIのAPIキーをセットする
        OPENAI_API_KEY = '[OpenAI API Keyに置き換えてください。]'
        openai.api_key = OPENAI_API_KEY
        self.database_name = database_name
        self.databas_id = None

        # タイトルの要約用のプロンプト
        self.title_summary_prompt = 'summarize the title in Japanese'
        # プロンプトを工夫してみましょう。精度が上がるかもしれません

        # コンテンツの要約用のプロンプト
        self.contents_summary_prompt = f"summarize the content for each paragraphs with three points in Japanese without '\n'"
        # プロンプトを工夫してみましょう。精度が上がるかもしれません。以下はその一例です。英語で書いた方が精度は良いです。
        # self.contents_summary_prompt = f"summarize the content for each paragraphs in Japanese without '\n'. \
        #     The content that is passed on is written in markdown format.\
        #         In addition, please adhere to the following format.\
        #             ## Format:\
        #                 # [brief summary of the first paragraph]\
        #                     ## [first point of detail summary of the first paragraph]\
        #                         ## [second point of detail summary of the first paragraph] - optional\
        #                             ## [third point of detail summary of the first paragraph] - optional\
        #                 # [brief summary of the second paragraph]\
        #                     and so on..."

        # Notionデータベースのカラム関係の設定
        # * ここは、データベースを作成するときに、自動で作成するようにしたい。今後のアップデートに期待。
        # 要約するページが格納されるデータベースのカラム名
        self.summary_target = "Name"
        # 1行要約を入れるカラム名
        self.one_line_summary = "One-line Summary"
        # 詳細要約を入れるカラム名
        self.detail_summary = "Summary"
        # タグを格納するカラム名
        # self.tags = "Tags" #? 今後の機能改善で、文章からタグを自動でつける機能を実装予定。

    def get_database_id(self):
        """データベースIDを取得するための関数

        Args:

        Returns:
            _type_: データベースがあれば、そのIDをself.database_idに保存。なければNone
        """
        result = self.notion.search(
            filter={"property": "object", "value": "database"}).get("results")
        for db in result:
            if db["title"][0]["text"]["content"] == self.database_name:
                self.database_id = db["id"]
        return None

    def find_page_in_database(self, title):
        results = self.notion.databases.query(
            **{
                "database_id": self.database_id,
                "filter": {
                    "property": self.summary_target,
                    "title": {
                        "equals": title
                    }
                }
            }
        ).get("results")

        return results[0]["id"] if len(results) > 0 else None

    # * データベースのOne-line Summary列とSummary列を作成しているが、別のデータベースを作って、そこに追加する関数にする？
    # * Summary列に、ページタイトルをtitle, 要約をそのページの中身としてcontentを渡すようにしたかったが、Notionデータベースの設計上、Summary列はテキスト列なのでページを追加できないらしい。
    # ? ページリンクならいけるかもだから、それで作る？
    # * これいらない。
    def add_page_to_database(self, one_line_summary, detail_summary):
        """データベースにページ（行）を追加する関数

        Args:
            title (_type_): 追加したいタイトル。一行要約が入る。One-line Summary列に追加。
            content (_type_): 追加したい要約。Summary列に追加。
        """
        new_page = {
            self.one_line_summary: {"rich_text": [{"text": {"content": one_line_summary}}]},
            self.detail_summary: {"rich_text": [
                {"text": {"content": detail_summary}}]}
        }
        self.notion.pages.create(
            parent={"database_id": self.database_id}, properties=new_page)

    def update_page_in_database(self, page_id, one_line_summary, detail_summary):
        if detail_summary == "":
            detail_summary = 'このページはクローリング禁止のため、ページ内容を取得できませんでした。\
                または、まだ記事の内容を取得できていない可能性があります。\
                時間をおいて再度実行してみて下さい。'
        updates = {
            self.one_line_summary: {"rich_text": [{"text": {"content": one_line_summary}}]},
            self.detail_summary: {"rich_text": [
                {"text": {"content": detail_summary}}]}
        }
        try:
            self.notion.pages.update(page_id, properties=updates)
        except:
            updates = {
                self.one_line_summary: {"rich_text": [{"text": {"content": one_line_summary}}]},
                self.detail_summary: {"rich_text": [
                    {"text": {"content": '元の文章が長すぎてNotionデータベースに保存できません。申し訳ありません。'}}]}
            }
            self.notion.pages.update(page_id, properties=updates)

    # ここに要約する処理を書く
    def get_completion(self, prompt, model="gpt-3.5-turbo", temperature=0):
        """OpenAIのAPIを使用して文章を生成する関数

        Args:
            prompt (_type_): プロンプト
            model (str, optional): 使用するモデル. Defaults to "gpt-3.5-turbo".
            temperature (int, optional): どれだけランダムに回答を生成するか。数字が大きいほどランダム. Defaults to 0.

        Returns:
            _type_: 生成された文章
        """
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message["content"]

    def chunk_text(self, text, chunk_size=3000):
        """テキストを指定した文字数で分割する関数
        Args:
            text (_type_): 分割したいテキスト
            chunk_size (int, optional): 分割する文字数. Defaults to 4000.

        Returns:
            _type_: 分割されたテキストのリスト
        """
        words = text.split()
        chunks = []
        current_chunk = []

        for word in words:
            if len(" ".join(current_chunk)) + len(word) + 1 <= chunk_size:
                current_chunk.append(word)
            else:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def summarize_title(self, text):
        """要約したタイトルを日本語で返す関数

        Args:
            text (_type_): 要約したいテキスト

        Returns:
            _type_: 要約された記事のタイトル
        """
        prompt = f"{self.title_summary_prompt} : {text}"
        summary = self.get_completion(prompt, temperature=0)
        return summary.strip()

    def summarize_content(self, text):
        """要約した本文を日本語で返す関数。現状、本文を3つの段落に分けて日本語で生成するようにしている。
        Args:
            text (_type_): 要約したいテキスト

        Returns:
            _type_: 要約された記事の本文
        """
        paragraphs = text.split("\n\n")
        summarized_paragraphs = []
        for paragraph in paragraphs:
            chunks = self.chunk_text(paragraph)
            summarized_chunks = []
            for chunk in chunks:
                prompt = f"{self.contents_summary_prompt}: {chunk}"
                summary = self.get_completion(prompt, temperature=0)
                summarized_chunks.append(summary.strip())
            summarized_paragraphs.append(" ".join(summarized_chunks))

        return "\n\n".join(summarized_paragraphs)

    def summarize_file(self, dict_data):
        """summarize_titleとsummarize_contentを呼び出して、要約を作り、辞書で返す関数
        Args:
            dict_data (dict): 要約したいテキストの辞書。キーがタイトル、バリューが本文。
        """
        summary = {}
        for title, content in dict_data.items():
            summary_title = self.summarize_title(title)  # キーであるタイトルを要約
            # バリューである本文を要約
            summary_content = self.summarize_content(content)
        summary[summary_title] = summary_content
        return summary

    # summary_resultの内容をデータベースに追加する関数

    def add_summary_to_database(self, title, result_summarize):
        for one_line_summary, detail_summary in result_summarize.items():
            page_id = self.find_page_in_database(title)
            self.update_page_in_database(
                page_id, one_line_summary, detail_summary)
            print("Summarize added to the database.")

    def get_all_blocks(self, page_id):
        all_blocks = []
        next_cursor = None
        has_more = True

        while has_more:
            response = self.notion.blocks.children.list(
                page_id,
                start_cursor=next_cursor,
                page_size=100  # 1リクエストあたりの最大ブロック数 (最大100)
            )
            all_blocks += response["results"]
            next_cursor = response.get("next_cursor")
            has_more = response.get("has_more")

        return all_blocks

    def get_all_pages(self):
        """データベースの全てのページを取得する関数

        Args:

        Returns:
            articles (dict): まだ要約していないページの記事の題名と本文を格納した辞書
        """
        self.get_database_id()
        pages = self.notion.databases.query(
            database_id=self.database_id)['results']

        # 各ページから名前（Name）列の文字列とページ内の文章を取得。Summary列が空欄の場合のみ取得
        # この中に要約して辞書に足す処理を書く
        for page in tqdm(pages):
            # 記事を格納する辞書
            articles = {}
            # Summary列が空欄ではない場合はスキップ
            if page["properties"][self.detail_summary]["rich_text"] != []:
                continue
            # 名前（Name）列の文字列を取得
            title = page["properties"][self.summary_target]["title"][0]["text"]["content"]
            articles[title] = []

            # ページIDを使用してページの詳細情報を取得
            page_id = page["id"]
            # page_details = self.notion.pages.retrieve(page_id)

            # ページ内の文章を抽出
            blocks = self.get_all_blocks(page_id)

            # 記事の内容をcontentsに格納し、articlesに追加
            contents = []
            for block in blocks:
                # 平文
                if block["object"] == "block" and block["type"] == "paragraph":
                    paragraph_text = block['paragraph']['rich_text'][0]['text']['content']
                    contents.append(paragraph_text)
                # H1
                elif block['object'] == 'block' and block['type'] == 'heading_1':
                    paragraph_text = block['heading_1']['rich_text'][0]['text']['content']
                    contents.append(" # " + paragraph_text + " ")
                # H2
                elif block['object'] == 'block' and block['type'] == 'heading_2':
                    paragraph_text = block['heading_2']['rich_text'][0]['text']['content']
                    contents.append(" ## " + paragraph_text + " ")
                # H3
                elif block['object'] == 'block' and block['type'] == 'heading_3':
                    paragraph_text = block['heading_3']['rich_text'][0]['text']['content']
                    contents.append(" ### " + paragraph_text + " ")
                # リストアイテム
                elif block['object'] == 'block' and block['type'] == 'bulleted_list_item':
                    paragraph_text = block['bulleted_list_item']['rich_text'][0]['text']['content']
                    contents.append(" * " + paragraph_text + " ")
                # 番号付きリスト
                elif block['object'] == 'block' and block['type'] == 'numbered_list_item':
                    paragraph_text = block['numbered_list_item']['rich_text'][0]['text']['content']
                    contents.append(" * " + paragraph_text + " ")
            contents = ''.join(contents)
            # * contentsが何もなかったら、その旨を記載。（クローリング禁止とか対策しているサイトはSave to Notionがページ内容を取得できないっぽい。）
            articles[title] = contents
            # データベースに追加する
            result_summarize = self.summarize_file(articles)
            self.add_summary_to_database(
                title, result_summarize)
        return articles

    def main(self):
        self.get_all_pages()


if __name__ == "__main__":
    DATABASE_NAME = '[Notionのデータベース名に置き換えて下さい。]'
    notion_summarizer = NotionSummarizer(DATABASE_NAME)
    notion_summarizer.main()
