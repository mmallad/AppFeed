__author__ = 'Dpak Malla'

from lib.Db.Database import  Database


class Records(Database):
    def __init__(self):
        try:
            Database.__init__(self, "localhost", "root", "cdanged", "appfeed")
            self.errorMsg = None
        except Exception, e:
            raise Exception(e)

    def Execute(self, query, value=()):
        try:
            if value:
                self.cursor.execute(query, value)
            else:
                self.cursor.execute(query)
        except Exception, e:
            raise Exception(e)

    def Save(self):
        self.getConnection().commit()

    def Cancel(self):
        self.getConnection().rollback()

    def RowCount(self):
        return int(self.cursor.rowcount)

    def Fetch(self):
        try:
            return self.cursor.fetchall()
        except Exception, e:
            raise Exception(e)

if __name__ == 'main':
    print 'Not allowed for this script.'
