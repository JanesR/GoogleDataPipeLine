from google.cloud import storage
class CloudStorage():
    def __init__(self) -> None:
        pass

    def SendToBucket(self,bucketName,fileName):
        client = storage.Client()
        bucket = client.get_bucket(bucketName)
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
        return True