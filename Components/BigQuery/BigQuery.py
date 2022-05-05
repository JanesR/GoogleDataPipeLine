from google.cloud import bigquery

class BigQuery():
    def __init__(self) -> None:
        pass
        

    def LoadTableFromParquet(self,bucketName,fileName,tableId,isIncrement):
        retInfo = False
        client = bigquery.Client()
        write_disposition = ""

        if isIncrement:
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND
        else:
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE

        job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.PARQUET,write_disposition=write_disposition)
        uri = "gs://"+bucketName+"/"+fileName
        load_job = client.load_table_from_uri(uri, tableId, job_config=job_config)
        load_job.result()
        destination_table = client.get_table(tableId)
        print("Loaded {} rows.".format(destination_table.num_rows))
        retInfo = destination_table.num_rows > 0
        return retInfo
