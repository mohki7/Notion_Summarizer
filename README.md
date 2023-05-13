# Notion Summarizer README

**※必ず注意事項を理解した上で使用してね。責任は一切持ちません。APIキーを使いすぎるとお金がかかるので注意しましょう**

※普通に行けば全体で15-20分くらいでセットアップが完了します。

※プログラミングが多少わかる人向けに、「エンジニア向けのshort README」も作成しました。目次から飛んでみてね

※このREADMEも、プログラム自体も、アップデートしていく予定です。

**※手取り足取り説明を書いたら長くなってしまいましたが、難しいことは何もありません。時間もそんなにかかりません。ご安心を。**

※何か不明点や間違っている部分があれば、大木までLINEもしくはインスタのDMください

# 使い方の詳細

## 必要なもの

- ChatGPTのAPIキー（従量課金制。ただ、最初の3ヶ月間だけ$18までは無料。らしい。）
    - [ChatGPTのAPIキーの取得方法](https://www.a-c-japan.com/solution/chatgpt/chatgpt-api/#:~:text=ChatGPT%20API%20%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95,-%EF%BD%9E%20ChatGPT%20API&text=%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E5%BE%8C%E3%80%81%E5%8F%B3%E4%B8%8A%E3%81%AE%E3%80%8CPersonal,%E5%A0%B4%E6%89%80%E3%81%AB%E4%BF%9D%E7%AE%A1%E3%81%97%E3%81%BE%E3%81%99%E3%80%82)
        
        [ChatGPTのAPIキーの取得の仕方｜Satomi](https://note.com/chronic/n/n79eb21b3654c)
        
        ここら辺を参考に、ChatGPTのAPIを取得してください。
        
        - [ ]  **ChatGPTのAPIキーは得られましたか？**
        
    - 最初の3ヶ月だけ$18まで無料らしい。
        
        [ChatGPTのAPIで何日経っても429エラーが返ってくるのは、APIの無料期間が終了していたからだった | 経験知](https://keikenchi.com/why-chatgpts-api-returns-429-error-even-after-many-days#:~:text=結論としては、どうやらAPI,3ヶ月のようです。)
        
    
    ※有料とは言っても、一般的な感覚で言えば激安です。GPT-3.5turboであれば、100円あれば膨大な量の文章を要約できるはずです。ここは調べて計算してみて下さい。
    
- Notion Integrationのトークン＆使用する「あとで読む」Notionデータベースのリンク
    - Notion Integrationの設定方法
        
        [Notion API を使用してデータベースを操作する](https://zenn.dev/kou_pg_0131/articles/notion-api-usage)
        
        この記事の「Notion APIを使ってみる」の手前までを準備して下さい。
        
        - [ ]  **Notion Integration Tokenは得られましたか？（secret_から始まるトークン）**
        - [ ]  **「あとで読む」Notionデータベースのリンクは得られましたか？**

ここまで終われば、あとはそれらを使ってセットアップするだけ！

## 具体的な設定のステップ

1. Notionで要約したいものを集めて格納するデータベースを用意する
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1cac219-7c50-41e2-9c37-ddffcda49317/Untitled.png)
    
    この画像のようなデータベースを用意して下さい。
    
    ※列の名前は同じでなくても構いません。
    
    ※写真には余計な列もあります。最低限必要な列は以下のチェックリストを参照して下さい。
    
    ※写真と同じ構図にしておくと、後々のセットアップが少しだけ楽になります。
    
    **必要な列：**
    
    - [ ]  [Name]列：Webサイトや論文がこの列にページとして格納されます
    - [ ]  [One-line Summary列]：題名が要約され、ここに格納されます
    - [ ]  [Summary列]：Name列の要約がここに格納されます
    - [ ]  [URL列]：Name列のURLがここに格納されます
    
    - [ ]  データベースを用意できましたか？
    
2. Chromeに「Save to Notion」もしくは「Notion Web Clipper」をインストールし、1で作成したデータベースに追加できるかを確認
    
    [Save to Notionの特徴と使い方を分かりやすく解説！ -](https://myokihissa.com/4851/)
    
    この記事の通りにやれば理解できるはずです。面倒な人は、Chrome拡張機能「Save to Notion」を検索し、ぽちぽちしてみて下さい。複雑なことは何もないので全然できると思います。
    
    - [ ]  Save to NotionもしくはNotion Web Clipperのインストールはできましたか？
    
    - Webサイトをデータベースに追加できるかを確認
    
    早速適当な記事をデータベースに追加してみましょう。
    
    ※クローリング、スクレイピング対策がされているサイトはタイトルのみが追加されてしまいます。そのようなサイトをこのツールを使って取得することはできないので、他のサイトにしましょう。
    
    追加できると、以下の写真のようになります。
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cd0d762-03da-4185-861c-9f843afa35b9/Untitled.png)
    
    しばらく待ち、追加した記事にカーソルを合わせると「OPEN」というボタンが出てきます。
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04d9bf88-3efb-4ce1-b5a4-000a1d83cb2f/Untitled.png)
    
    これは、データベースに格納した記事の中身がここにダウンロードされたことになります。
    
    OPENを押すと記事の中身が見られることを確認しましょう。
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/39fe95b0-2482-408f-ab05-631de34f9c54/Untitled.png)
    
    このページでサイトの中身が正しく表示されない場合、そのサイトはクローリング対策・スクレイピング対策がされており、取得できなかったことがわかります。その場合は諦めましょう。
    
    ※ただWebサイトの取得に時間がかかっているだけの場合もありますが、通常であれば1分ほどで表示されます。
    
    - [ ]  Save to NotionもしくはNotion Web Clipperにより、データベースに追加できましたか？
    
    ここまでは、Notionを日頃から使っている人ならば有名な便利ツールの使い方に過ぎません。
    
    僕はここにChatGPTのAPIを利用し、要約できるようにしました。
    
3. 配布したPythonプログラムを開く
    
    エディタはなんでも良いので、NotionSummarizer.pyを開きます。VSCodeがお勧めです。
    
    ※エンジニアではない方はここが大変かもしれませんが、ググればわかりやすい記事がたくさん出てくるので、pythonファイルを実行できる環境を用意しましょう。
    
    ※個人的にはVSCodeがお勧めです。
    
    ※Macならセッティングは比較的簡単にできます。Appleバンザイ。
    
    pythonファイルを開くと、写真のようになります。（VSCodeで開いた例）
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d825a28f-4de1-46fc-bde5-85d698f017aa/Untitled.png)
    
    - [ ]  Pythonファイルを開けましたか？
    
4. Notion Integration Tokenを打ち込む
    
    [Notion Integrationのトークン＆使用する「あとで読む」Notionデータベースのリンク](https://www.notion.so/Notion-Integration-Notion-2cdb06b8c44a48f587d5d36e125b5411) 
    
    ここで取得したNotion Integrationのトークンキーをプログラム内の指定の場所に貼り付けます。
    
    一番上の方にある「def __init__(self, database_name)」と書いてあるところを探して下さい。
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b824896d-3f5d-48fe-8ddc-3adc89202b0f/Untitled.png)
    
    そこの、NOTION_API_KEY=[Notion Integration Tokenに置き換えて下さい]にトークンを貼り付けます。
    
    []ごとトークンで置き換えます。トークンがaaaだとすると、
    
    ```python
    NOTION_API_KEY=’aaa’
    ```
    
    となるようにして下さい。
    

- [ ]  Notion Integration Tokenの設定は完了しましたか？

1. OpenAIのchatGPTのAPIを打ち込む
[ChatGPTのAPIキー（従量課金制。ただ、最初の3ヶ月間だけ$18までは無料。らしい。）](https://www.notion.so/ChatGPT-API-3-18-c44ce75f07564675a4b97f7ebe40de35) 
    
    4.と同様に、ここで取得したAPIキーを同様に打ち込みます。
    
    打ち込む場所は、4.で打ち込んだ場所のすぐ下にあります。
    
    - [ ]  chatGPTのAPIを打ち込みましたか？
    
2. 1. で作成したNotionのデータベースの名前を設定する
最後です。Notionデータベースの名前を設定しましょう。
データベースのすぐ上にある場所に表示されているはずです。（もしくは自分で設定）

    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04d9bf88-3efb-4ce1-b5a4-000a1d83cb2f/Untitled.png)
    
    この場合、「Read Later Summary」がデータベース名になります。
    
    これを、プログラムの一番下にある「DATABASE_NAME」に打ち込みます。
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/135f40b2-586c-435c-8be6-c76fcc059cd0/Untitled.png)
    
    ```python
    DATABASE_NAME = 'Read Later Summary'
    ```
    
    このようになるようにします。
    
    - [ ]  Notionデータベースの設定が完了しましたか？
    
3. 実行する
設定、お疲れ様でした。あとは実行するだけです。
ターミナルを開いて、「python NotionSummarizer.py」と入力し、Enterを押します。

ターミナルの開き方は上のツールバーの「ターミナル」から「新しいターミナル」を選択して下さい。
[https://www.javadrive.jp/vscode/terminal/index1.html#:~:text=ターミナルを開くには,ターミナルは Windows PowerShell です。](https://www.javadrive.jp/vscode/terminal/index1.html#:~:text=%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%82%92%E9%96%8B%E3%81%8F%E3%81%AB%E3%81%AF,%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%AF%20Windows%20PowerShell%20%E3%81%A7%E3%81%99%E3%80%82)
わからない場合はこの記事を参考にすればすぐにわかります。

実行が成功すると、ターミナルにプログレスバーのようなものが表示されます。
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d2bd572-a5d5-4a88-aee0-3e3e64da085f/Untitled.png)
    
    この状態になれば、あとは待つだけです。おめでとうございます。
    
    しばらく待つと、Notionのデータベースに以下のように要約が入っているはずです。
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/434e6053-a7f3-44fa-b40c-1d84e7fc96f1/Untitled.png)
    
    お疲れ様でした。🎉
    
    ※**エラーが出る場合**
    
    特にエンジニアではない人はエラーが出ると思います。以下の「プログラム実行に必要なライブラリ」に書いてあるコードをターミナルに打ち込み、実行して下さい。
    
    [プログラム実行に必要なライブラリ](https://www.notion.so/9659757294584fdabc0a963c5e34e643) 　　
    
    ※**よくあるエラー**
    
    エラーの理由がわからない場合、以下を参考にして下さい。
    
    [よくあるエラー](https://www.notion.so/d44873e9c6844c65845019c94d7a3141) 
    
    - [ ]  pythonファイルを実行できましたか？
        
        
    
    ### プログラム実行に必要なライブラリ
    
    - notion-client
        
        ```python
        pip install notion-client
        ```
        
    - openai
        
        ```python
        pip install openai
        ```
        
    - tqdm
        
        ```python
        pip install tqdm
        ```
        
4. プロンプトを調整する
    
    さて、出てきた要約は正しかったでしょうか？要約の長さ、精度、フォーマットは要望通りだったでしょうか？
    
    この部分を大きく作用するのが、「プロンプト」です。要約にはChatGPTを使用しているので、うまくChatGPTに指示を与えられれば与えられるほど、良い出力が返ってきます。（ChatGPTを日頃から使っている人はすごくよくわかると思います。）
    
    **プロンプトは、Notion Integration TokenやChatGPTのAPIキーを入れたdef __init__(self, database_name)のところで編集できるようにしてあります。積極的にいじって試してみましょう。**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/468cec28-4e1a-4c8a-b1c8-fd6cae88b47a/Untitled.png)
    
    このツールも良いプロンプトを入れれば入れるほど、良い要約が返ってきます。
    
    論文などの長い文章を要約しようとすると、「データベースに格納しきれませんでした」という旨の文章が表示されるようにしてありますが、これもプロンプトが悪いせいです。
    
    文字数制限を入れたり、短いフォーマットで出力されるような工夫をしてみましょう。
    
    プロンプトについて詳しく知りたい人は、ネットに山ほど情報が転がっているので参考にしてみて下さい。
    
    **うまく文章を要約できるようなプロンプトを、ChatGPTに考えてもらうのも一つの手です。**
    
    これにて、チュートリアルは終了です。次回からこのツールを使用するときは、プログラムを実行するだけです。まとめたステップは以下のブロックを参考にして下さい
    
    [実際に使うときのステップ（まとめ）](https://www.notion.so/db531036cb8641d6ad84248592ba6d84) 
    

## 実際に使うときのステップ（まとめ）

1. Save to NotionなどでWebサイトや論文をデータベースに格納
2. 少し待つ。（Save to Notionの実行完了待ち）※待ってもページ内に追加されない場合、スクレイピング出来ないサイトの可能性があります。その場合、要約はできません。
3. プログラムを実行
4. 少し待つ（Webサイトなら1記事あたり30秒ほど、論文は3分ほど）
5. 要約と1行要約の欄が埋まれば、無事成功
6. しばらく待っても追加されない場合、Pythonプログラムにエラーが出ていないか確認してください。
7. うまくできない場合は、プロンプトをいじるべし。

### プロンプトの例

### プロンプトを勉強できるサイト

どちらも高度なプロンプトまで紹介されていますが、簡単なテクニックを身につけるだけで十分です。

より自由に扱いたい場合はReActやLangChainなどの高度な手法にもチャレンジしてみて下さい。

[ChatGPT プロンプトエンジニアリング – Nextra](https://www.promptingguide.ai/jp/models/chatgpt)

[サクッと始めるプロンプトエンジニアリング【LangChain / ChatGPT】](https://zenn.dev/umi_mori/books/prompt-engineer)

# エンジニア向けのshort README

エンジニアの方は詳細な説明もいらないと思うので、概略を示します。

1. 必要なものを準備して下さい。
    
    [必要なもの](https://www.notion.so/91c477616f3d4e058036571dbf78e16b) 
    
    - [ ]  Notion Integration Token
    - [ ]  OpenAI ChatGPTのAPIキー
    
    [具体的な設定のステップ](https://www.notion.so/809193b0a5914488909ed881d6714610) 
    
    - [ ]  要約を入れるデータベース
    - [ ]  Chrome拡張機能「Save to Notion」
2. Notionのデータベースを用意します
3. 配布したpythonファイルを開きます
4. イニシャライザ関数内の指定の場所にNotion Integration TokenとChatGPTのAPIキーを入力して下さい
5. Notionデータベースの名前を最後のif \__name__ == ‘__main__’内のDATABASE_NAMEに入力して下さい。
6. 実行してください
7. 基本的なエラー解決はできるはずです。頑張って下さい。よくあるエラーも参考にして下さい。
8. Notionデータベースに要約が追加されていれば、完了です。お疲れ様でした。

## よくあるエラー

- Notionのデータベースに空欄の行がある
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f0ad2df0-adfc-41cc-9bcd-ab4c6a65d0c9/Untitled.png)
    
    Notionのデータベースを確認してください。空欄の行があるとこのようなエラーが表示されます。
    
    空欄の行を削除して再度実行して下さい。
    

- トークンオーバー
    - プロンプトを長く設定してしまうと、トークンエラーになってしまうので、エラーと様子を見ながら調整する必要があります。
        - これもGPT-4にアップグレードすれば一回に読み込めるトークンが増えるので改善が見込まれます。
        - ※一応、チャンク数を小さくすることで回避を試みることもできますが、一回に要約する文章量が少なくなり、要約の精度が落ちかねないのでお勧めしません。
    - プロンプトを短くしてみましょう。
    
- 要約文字数オーバー
    - Notionデータベースに保存できる要約の長さは2000字までなので、そこもプロンプトエンジニアリングで調整が必要です。
        - notionなんとか〜≤2000みたいなエラーが出たらそれなので、短い要約をするように指示しましょう

# **注意事項（必ず読んでね）**

- 与えるプロンプトによって、精度が大きく作用されます。良いプロンプトを与えるようにしましょう
- スクレイピングが出来ないものは使用できません
- APIキーをGPT-4にすることによって、大きく改善されることが期待されます。ただ、まだ使えないのでウェイティングリストに追加して待ちましょう。
    
    [GPT-4 API waitlist](https://openai.com/waitlist/gpt-4-api)
    
- 従量課金なので、ちょくちょく使用量を確認してね。でも割とたくさん要約しても、無料で使えるはずです。
- **無断の二次配布・商用利用を禁止します。トラブルの責任は一切持ちません。**

まとめると、

- 良いプロンプトを与え、GPT-4のAPIにすると精度が上がることが期待される。多少精度が悪いのは仕方ないこと。
- 従量課金なので気をつけてね。でもよっぽど長い文章を入れない限り、いきなり大量に一気に課金されるようなことはないはず。

以上です。お疲れ様でした。
