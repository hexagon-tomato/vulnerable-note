# flash をインポートに追加
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = conn.execute(query).fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['username'] = user['username'] # ★ ユーザー名もセッションに保存

            # ★ フラッシュメッセージを追加
            flash('ログインに成功しました！', 'success') 

            return redirect(url_for('index'))
        else:
            error = 'ユーザー名またはパスワードが正しくありません。'
            flash(error, 'danger') # エラーメッセージもフラッシュで表示

    return render_template('login.html')

# ★ ログアウトルートを追加
@app.route('/logout')
def logout():
    # セッションをクリアする
    session.clear()
    flash('ログアウトしました。', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)