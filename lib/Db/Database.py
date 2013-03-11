__author__ = 'Dpak Malla'

import MySQLdb

class Database:
    def __init__(self,host,user,password,db):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db
        try:
            self.__connection = MySQLdb.connect(host=self.__host,user=self.__user,passwd=self.__password,db=self.__db)
            self.cursor = self.__connection.cursor(MySQLdb.cursors.DictCursor)
        except Exception, e:
            self.__connection.close()
            raise Exception('Error',e)
    def __del__(self):
        try:
            self.__connection.close()
        except Exception:
            pass
    def close(self):
        self.__connection.close()
    def getConnection(self):
        return self.__connection;

if __name__ == 'main':
    print 'Not allowed for this script'
