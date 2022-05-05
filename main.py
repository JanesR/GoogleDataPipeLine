from Components.DataBase.SourceTypes import SourceTypes
from Components.OperationFiles.OperationFiles import OperationFiles
from Components.CloudStorage.CloudStorage import CloudStorage
from Components.BigQuery.BigQuery import BigQuery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

def main():

    server = "localhost"
    userName = "root"
    passWord = ""
    dataBase = "googleTeste"
    fileName = "testeFile.parquet"
    bucketName = "jr_bucket_test"
    tableId =  "projeto001-348115.mydataset_parquetProject.Persons"
    query = "select Personid,FirstName,LastName from Persons"

    fileOperator = OperationFiles()
    storageOperator = CloudStorage()
    bigQueryOperator = BigQuery()
    
    isCreatedFile = fileOperator.GenerateParquetFile(sourceType=SourceTypes.MYSQL,server=server,userName=userName,passWord=passWord, dataBase=dataBase,query=query,fileName=fileName)
    isSentToBucket = False
    if isCreatedFile:
        isSentToBucket = storageOperator.SendToBucket(bucketName=bucketName,fileName=fileName)
    
    if isSentToBucket:
        bigQueryOperator.LoadTableFromParquet(bucketName=bucketName,fileName=fileName,tableId=tableId,isIncrement=False)
    


if __name__ == "__main__":
    main()