# render_template をインポート
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): # 関数名をhello_worldからindexに変更（分かりやすくするため）
    # templatesフォルダのindex.htmlを探して表示する
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)