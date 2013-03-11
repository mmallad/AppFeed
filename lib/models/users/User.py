from lib.Db.Records import Records
import re


class User:
    def setUid(self, value):
        self.__UID = value
        return self

    def getUid(self):
        return self.__UID

    def setUsername(self, value):
        self.__USERNAME = value
        return self

    def getUsername(self):
        return self.__USERNAME

    def setPassword(self, value):
        self.__PASSWORD = value
        return self

    def getPassword(self):
        return self.__PASSWORD

    def __validate(self):
        if re.match('^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', self.__USERNAME) is None:
            raise Exception('Error', 'Invalid username.')
        if len(self.__PASSWORD) < 6:
            raise Exception('Error', 'Invalid password.')

    def Update(self):
        try:
            pass
        except Exception, e:
            raise Exception(e)

    def Save(self):
        try:
            self.__validate()
            query = "INSERT INTO tblUser (UID,USERNAME,PASSWORD)" \
                    " VALUES(%s,%s,%s)"
            self.__connection.Execute(query, (self.__UID, self.__USERNAME, self.__PASSWORD))
            return self.__connection.RowCount()
        except Exception, e:
            raise Exception(e)

    def Authenticate(self):
        try:
            tempU = self.__USERNAME
            self.__USERNAME = '**'
            tempP = self.__PASSWORD
            self.__PASSWORD = ''
            query = "SELECT * FROM tblUser WHERE USERNAME = %s AND PASSWORD = %s"
            self.__connection.Execute(query, (tempU, tempP))
            self.__Fill(self.__connection.Fetch())
            if self.__connection.RowCount() == 1 and self.__USERNAME == tempU and self.__PASSWORD == tempP:
                return True
            else:
                return False
        except Exception, e:
            raise Exception(e)

    def __Fill(self, data):
        for d in data:
            self.__UID = d["UID"]
            self.__USERNAME = d["USERNAME"]
            self.__PASSWORD = d["PASSWORD"]

    def FetchUsers(self, uid=None, email=None, username=None):
        try:
            if uid is not None:
                query = "SELECT * FROM tblUser WHERE UID = %s"
                self.__connection.Execute(query, (uid))
            elif username is not None:
                query = "SELECT * FROM tblUser WHERE USERNAME = %s"
                self.__connection.Execute(query, (username))
            else:
                pass
            self.__Fill(self.__connection.Fetch())
        except Exception, ex:
            raise Exception(ex)

    def __init__(self, uid=None):
        self.__connection = None
        try:
            self.__connection = Records()
            self.__USERNAME = None
            self.__UID = None
            if uid is not None:
                self.FetchUsers(uid)
        except Exception, e:
            raise Exception(e)