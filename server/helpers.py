import json
import datetime

import datetime

def write_log(message, log_file='applog.txt'):
    """
    Write a log message to the specified log file.

    :param message: The log message to write.
    :param log_file: The file to which the log message should be written. Default is 'app.log'.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as file:
        file.write(f"[{timestamp}] {message}\n")

def run_gpt4():
    import openai
    import json
    import os
    from pathlib import Path
    script_location = Path(__file__).absolute().parent

    file_location = script_location / 'creds.json'

    with open(file_location, "r") as file:
        credentials = json.load(file)
    openai.api_key = credentials["OPENAI_API_KEY"]
    # Generate a question using OpenAI API.
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "以下に受け取ったメールをできるだけ文章を変えずにもっと読みやすく、してください."},
                {"role": "assistant", "content": f"""monopo様、

初めまして、突然の連絡申し訳ありません。
加藤太一と申します。

NY近辺Amherst Collegeで数学とコンピュータサイエンスを専攻しておりテックコンサルタントとのしての活動を高校生時代からおこなってきており、マイクロソフト、メルカリ、チームラボ等々の会社で幅広いソフトウェア開発関連のお仕事をさせていただいてきております。

ただ、高校の頃からクリエイティブなことが好きで趣味で写真を撮ったり、自分のアプリをデザインしてマーケティングしたりとinterdisciplinerayに活動をしてきました。そこで、デジタルエクスペリエンスの仕事に興味を持ち、ある日本のビジネス誌を読んでいたときにmonopoに巡り合いました。「個々が持っているクリエイティビティが最大限に発揮され、自由にコラボレーションできる場」という言葉が心に響き、どの様な形でmonopoさんと一緒にお仕事をできるか、と考えていました。私の持っているスキルとしてはウェブ・デジタルテクノロジーを使ったビジュアルエクスペリエンス、またデータを活用したインタラクティブエクスペリエンスのお仕事等が向いていると思いますがどんどんと新しいことに調整していきたいと考えています。もちろん日本語と英語もネイティブレベルで書いて喋れます。

是非お話しを伺いたいのですが、今月いつかお時間いただけないでしょうか。金曜日であればNYCでのミーティング可能ですので是非実際にお会いできたら嬉しいです。

加藤"""}],
            temperature=0.5
        )
        result = response.choices[0].text.strip()
        write_log(response)
    except Exception as e:
        write_log(json.dumps({"error": "Internal error. %s" % e.__str__()}))
