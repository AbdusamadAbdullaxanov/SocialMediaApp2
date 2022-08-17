import sqlite3

connection = sqlite3.connect("homework.db")
cursor = connection.cursor()
# for i in range(10):
#     cursor.execute(
#         """INSERT INTO user (name, email, password) VALUES (?, ?, ?)""",
#         (f"name {i}", "email", "asdasdasd")
#     )

cursor.execute(
    """CREATE TABLE IF NOT EXISTS user (
    id INTEGER, name TEXT, email TEXT,
    password TEXT, PRIMARY KEY ("id"))
    """)

cursor.execute("""DELETE FROM user WHERE name='name 9'""")
connection.commit()
