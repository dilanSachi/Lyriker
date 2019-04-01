import sqlite3

class SQLiteConnector():

    def __init__(self, aContext):
        self.aContext = aContext
        self.database = self.aContext.get_resource('lyriker.db')

    def checkDB(self):
        print('a')
        stmt = 'select * from users'
        userdata = self.readDB(stmt)
        print(userdata)
        if(userdata == False or userdata == [('','')]):
            print('c')
            stmt = '''create table users
                    (username text, email text unique, primary key(username))'''
            self.createTable(stmt)
            return False
        return True

    def createTable(self, stmt):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute(stmt)
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def executeMany(self, statement, arr):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.executemany(statement, arr)
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def executeOne(self, statement, values):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute(statement, values)
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def readDB(self, statement):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute(statement)
            allRows = cursor.fetchall()
            conn.close()
        #for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns email column.
            #print('{0} : {1}'.format(row[0], row[1]))
            return allRows
        except:
            return False
