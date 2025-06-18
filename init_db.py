import sqlite3

# データベースに接続（なければ、database.dbというファイルが作られる）
connection = sqlite3.connect('database.db')

# データベース操作のためのカーソルを作成
cursor = connection.cursor()

# usersテーブルを作成
# IF NOT EXISTS をつけると、既にテーブルがあってもエラーにならない
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# 初期データを投入（既にあってもエラーにならないように工夫）
# 通常、パスワードを平文で保存するのは絶対にNGだが、今回は脆弱性を作るためあえて行う
initial_users = [
    ('admin', 'password123'),
    ('user1', 'password')
]

for user in initial_users:
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", user)


# 変更をコミット（保存）
connection.commit()
# 接続を閉じる
connection.close()

print("データベースの初期化が完了しました。")