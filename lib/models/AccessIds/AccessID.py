__author__ = 'Dipak Malla'

from lib.Db.Records import Records


class AccessID:
    def setAccessId(self, value):
        self.__ACCESSID = value
        return self

    def getAccessId(self):
        return self.__ACCESSID

    def setAccessName(self, value):
        self.__ACCESSNAME = value
        return self

    def getAccessName(self):
        return self.__ACCESSNAME

    def __validate(self):
        pass

    def Save(self):
        try:
            self.__validate()
            query = "INSERT INTO tblAccessID (ACCESSID,ACCESSNAME)" \
                    " VALUES(%s,%s)"
            self.__connection.Execute(query, (self.__ACCESSID, self.__ACCESSNAME))
            self.__connection.Save()
            return self.__connection.RowCount()
        except Exception, e:
            self.__connection.Cancel()
            raise Exception(e)

    def __Fill(self, data):
        rv = list()
        for d in data:
            o = AccessID()
            o.setAccessId(d["ACCESSID"])
            o.setAccessName(d["ACCESSNAME"])
            rv.append(o)
        return rv

    def FetchAccess(self, accessID=None):
        try:
            if accessID is not None:
                query = "SELECT * FROM tblAccessID WHERE ACCESSID = %s"
                self.__connection.Execute(query, (accessID))
            else:
                query = "SELECT * from tblAccessID"
                self.__connection.Execute(query)
            return self.__Fill(self.__connection.Fetch())
        except Exception, ex:
            raise Exception(ex)

    def __init__(self, accessID=None):
        self.__connection = None
        try:
            self.__connection = Records()
            self.__ACCESSID = None
            self.__ACCESSNAME = None
            if accessID is not None:
                self.FetchAccess(accessID)
        except Exception, e:
            raise Exception(e)