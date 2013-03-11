__author__ = 'Dipak Malla'

from lib.Db.Records import Records


class Pro:
    def setProId(self, value):
        self.__PROID = value
        return self

    def getProId(self):
        return self.__PROID

    def setProName(self, value):
        self.__PRONAME = value
        return self

    def getProName(self):
        return self.__PRONAME

    def setProQry(self, value):
        self.__PROQRY = value
        return self

    def getProQry(self):
        return self.__PROQRY

    def __validate(self):
        pass

    def Save(self):
        try:
            self.__validate()
            query = "INSERT INTO tblPro (PRONAME,PROQRY)" \
                    " VALUES(%s,%s)"
            self.__connection.Execute(query, (self.__PRONAME,self.__PROQRY))
            self.__connection.Save()
            return self.__connection.RowCount()
        except Exception, e:
            self.__connection.Cancel()
            raise Exception(e)

    def __Fill(self, data):
        rv = list()
        for d in data:
            o = Pro()
            o.setProId(d["PROID"])
            o.setProName(d["PRONAME"])
            o.setProQry(d["PROQRY"])
            rv.append(o)
        return rv

    def FetchPro(self, proID=None, proName=None):
        try:
            if proID is not None:
                query = "SELECT * FROM tblPro WHERE PROID = %s"
                self.__connection.Execute(query, proID)
            elif proName is not None:
                query = "SELECT * from tblPro WHERE PRONAME = %s"
                self.__connection.Execute(query, proName)
            else:
                query = "SELECT * from tblPro"
                self.__connection.Execute(query)
            return self.__Fill(self.__connection.Fetch())
        except Exception, ex:
            raise Exception(ex)

    def __init__(self, proID=None):
        self.__connection = None
        try:
            self.__connection = Records()
            self.__PROID = None
            self.__PRONAME = None
            self.__PROQRY = None
            if proID is not None:
                self.FetchPro(proID)
        except Exception, e:
            raise Exception(e)