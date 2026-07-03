import sqlite3

conn = sqlite3.connect("chat_logs.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_message TEXT,
bot_reply TEXT
)
""")

cursor.execute("""
INSERT INTO chats(user_message, bot_reply)
VALUES(
'Hello',
'Hello! Welcome to the Advanced AI Chatbot.'
)
""")

conn.commit()

print("Database created and one chat saved successfully!")

conn.close()
