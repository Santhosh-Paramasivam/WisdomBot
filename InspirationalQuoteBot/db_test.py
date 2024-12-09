import sqlite3

connection = sqlite3.connect("inspirational_quotes.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM quotes")

allQuotes = cursor.fetchall()

print(allQuotes)

cursor.execute("SELECT count(quote) FROM quotes")
print(cursor.fetchall())