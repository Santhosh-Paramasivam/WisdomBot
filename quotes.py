import sqlite3

formatForDiscord = lambda string:string.removesuffix("\n").strip()

connection = sqlite3.connect("wise_quotes.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS quotes")
cursor.execute("CREATE TABLE IF NOT EXISTS quotes(quote_number INTEGER PRIMARY KEY,quote TEXT);")
connection.commit()

with open("quotes.txt", "r") as infile:
   allQuotes = infile.readlines()
   aQNewlineless = []

   for string in allQuotes:
      aQNewlineless.append(formatForDiscord(string))

   count = 0
   for string in aQNewlineless:
      # stringList = [string]
      cursor.execute("INSERT INTO quotes(quote) VALUES(?)",(string,))
      connection.commit()
      # print(stringList)
      count+=1

   # print(count)
