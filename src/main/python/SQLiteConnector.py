import sqlite3

class SQLite():

    def __init__(self):
        self.db = sqlite3.connect('lyriker')
        self.cursor = self.db.cursor()

    def createDB(self):
        #self.db = sqlite3.connect(':memory:')
        # Creates or opens a file called mydb with a SQLite3 DB
        self.cursor.execute(''' drop table if exists words''')
        self.cursor.execute(''' drop table if exists connections''')
        self.cursor.execute('''
            CREATE TABLE words(word_id INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT)
        ''')
        self.cursor.execute('''
                    CREATE TABLE connections(conn_id INTEGER PRIMARY KEY AUTOINCREMENT, song INTEGER,
                     originalWordIndex INTEGER, wordIndex INTEGER,  FOREIGN KEY (wordIndex) REFERENCES words (id))
                ''')
        self.db.commit()

    def executeMany(self, statement, arr):
        cursor = self.db.cursor()
        cursor.executemany(statement, arr)
        #cursor.executemany(''' INSERT INTO words(word) VALUES(?)''', [["pusa"], ["miya"]])
        self.db.commit()

    def readDB(self):
        cursor = self.db.cursor()
        cursor.execute('''SELECT id, word from words''')
        #word = cursor.fetchone()  # retrieve the first row
        #print(word[1])  # Print the first column retrieved(user's name)
        all_rows = cursor.fetchall()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns email column.
            print('{0} : {1}'.format(row[0], row[1]))

    def joinDB(self, term):
        cursor = self.db.cursor()
        cursor.execute('''SELECT * from connections natural left join (select * from words where word=(?)) as A where word_id=wordIndex''', [term])
        #word = cursor.fetchone()  # retrieve the first row
        #print(word[1])  # Print the first column retrieved(user's name)
        all_rows = cursor.fetchall()
        return all_rows

    def dropTable(self):
        cursor = self.db.cursor()
        cursor.execute(''' drop table words''')

#sl = SQLite()

#sl.executeMany()
#sl.readDB()