from Components.DataBase.SourceTypes import SourceTypes
from Components.OperationFiles.OperationFiles import OperationFiles
from Components.CloudStorage.CloudStorage import CloudStorage
from Components.BigQuery.BigQuery import BigQuery
import os
import configparser

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

def main():
    config = configparser.ConfigParser()
    config.read('etlprocess.ini')

    server = config["ELTCONFIG"]["server"]
    userName = config["ELTCONFIG"]["userName"]
    passWord = config["ELTCONFIG"]["passWord"]
    dataBase = config["ELTCONFIG"]["dataBase"]
    fileName = config["ELTCONFIG"]["fileName"]
    bucketName = config["ELTCONFIG"]["bucketName"]
    tableId =  config["ELTCONFIG"]["tableId"]

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config["ELTCONFIG"]["credentials"]

    query = GenerateQuery()

    fileOperator = OperationFiles()
    storageOperator = CloudStorage()
    bigQueryOperator = BigQuery()
    
    isCreatedFile = fileOperator.GenerateParquetFile(sourceType=SourceTypes.MYSQL,server=server,userName=userName,passWord=passWord, dataBase=dataBase,query=query,fileName=fileName)
    isSentToBucket = False
    if isCreatedFile:
        isSentToBucket = storageOperator.SendToBucket(bucketName=bucketName,fileName=fileName)
    
    if isSentToBucket:
        bigQueryOperator.LoadTableFromParquet(bucketName=bucketName,fileName=fileName,tableId=tableId,isIncrement=False)
    
def GenerateQuery():
    queryRet = "select Personid,FirstName,LastName from Persons"
    return queryRet

if __name__ == "__main__":
    main()