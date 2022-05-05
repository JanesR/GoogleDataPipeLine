import Components.DataBase.DataBase as DataBase
import Components.DataBase.SourceTypes as SourceTypes
import Components.DataBase.DataBaseCredentials as DataBaseCredentials
import pandas as pd
from os.path import exists

class OperationFiles():
    def __init__(self) -> None:
        pass

    def GenerateParquetFile(self,sourceType,server,userName,passWord,dataBase,query,fileName) ->bool:

        #gera as credenciais
        dbCredentials = DataBaseCredentials.DataBaseCredentials(Server=server,User=userName,Password=passWord,DataBaseName=dataBase)
        #gera a conexao a partir das credenciais informadas
        conn = DataBase.DataBase(sourceType,dbCredentials=dbCredentials).CreateConection()       
        #gera do dataframe de conversão a partir da query informada
        dataFrame = pd.read_sql(query,conn)
        #converte o arquivo em parquet
        dataFrame.to_parquet(fileName)
        return exists(fileName)
