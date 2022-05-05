from Components.DataBase.DataBaseCredentials import DataBaseCredentials
from Components.DataBase.SourceTypes import SourceTypes
import sqlalchemy
class DataBase:
    def __init__(self,SourceType=SourceTypes,dbCredentials=DataBaseCredentials):
        self.__sourceType = SourceType
        self.__dbCredentials = dbCredentials
        self.__strConnect = ''
        self.generateConectionString()     
    
    def CreateConection(self):
        conn = sqlalchemy.create_engine(self.__strConnect)
        return conn


    def generateConectionString(self):
        if self.__sourceType == SourceTypes.MSSQL:
            self.__strConnect = 'mssql+pymssql://'+self.__dbCredentials.GetUser()+':'+self.__dbCredentials.GetPassword()+'@'+self.__dbCredentials.GetServer()+'/'+self.__dbCredentials.GetDataBase()
        elif self.__sourceType == SourceTypes.MYSQL:
            self.__strConnect = 'mysql+pymysql://'+self.__dbCredentials.GetUser()+':'+self.__dbCredentials.GetPassword()+'@'+self.__dbCredentials.GetServer()+'/'+self.__dbCredentials.GetDataBase()
        