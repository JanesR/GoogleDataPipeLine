class DataBaseCredentials:
    def __init__(self,Server,User,Password,DataBaseName) -> None:
        self.__Server = Server
        self.__User = User
        self.__Password = Password
        self.__DataBaseName = DataBaseName

    def GetServer(self):
        return self.__Server

    def GetUser(self):
        return self.__User
    
    def GetPassword(self):
        return self.__Password
    
    def GetDataBase(self):
        return self.__DataBaseName