__author__ = 'Dpak Malla'

from lib.models.users.User import User


class InitProfile:
    def __init__(self, uid=None, email=None, username=None):
        try:
            self.__ID = uid
            self.__EMAIL = email
            self.__USERNAME = username
            self.__user = User()
            if self.__ID is not None:
                self.__user.FetchUsers(uid=uid)
            elif self.__EMAIL is not None:
                self.__user.FetchUsers(email=email)
            elif self.__USERNAME is not None:
                self.__user.FetchUsers(username=username)
            else:
                raise Exception('Error', 'Could not initialize.')
        except Exception, ex:
            raise Exception(ex)

    def checkAccountStatus(self):
        try:
            return self.__user.getStatus()
        except Exception, ex:
            raise Exception(ex)