__author__ = 'Dipak Malla'

from lib.Db.Records import Records


class FeedData:
    def setQuery(self, value):
        self.__QRY = value
        return self

    def setData(self, value):
        self.__DATA = value
        return  self

    def __validate(self):
        pass

    def Save(self):
        try:
            self.__validate()
            self.__connection.Execute(self.__QRY, self.__DATA)
            self.__connection.Save()
            return self.__connection.RowCount()
        except Exception, e:
            self.__connection.Cancel()
            raise Exception(e)

    def __init__(self):
        self.__connection = None
        try:
            self.__connection = Records()
            self.__QRY = None
            self.__DATA = None

        except Exception, e:
            raise Exception(e)