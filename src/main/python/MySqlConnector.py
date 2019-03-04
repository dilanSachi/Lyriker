import mysql.connector

# Connect with the MySQL Server
class MySqlConnector():

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', database='lyriker')

    def executeQuery(self,query, *arg):
        curA = self.cnx.cursor(buffered=True)
        #print("hi")
        curA.execute(query, (arg))

        self.cnx.commit()
        return curA
        #cnx.close()