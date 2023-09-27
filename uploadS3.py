import logging
import boto3
from botocore.exceptions import ClientError
import os

#BUCKET QUE VAI SALVAR O ARQUIVO
BUCKET_NAME = "uploadboto"

#CAMINHO DO ARQUIVO PARA UPLOAD
Arquivo_UPLOAD = "C:\\Users\\juhlianna\\Documents\\PYTHON\\Manipular arquivos TXT com Python\\EXTRATO2023Mod.txt"
s3 = boto3.client("s3")

# LISTA TODOS OS BUCKETS
buckets_resp = s3.list_buckets()
for bucket in buckets_resp["Buckets"]:
    print(bucket)

def upload_file(FILE_UPLOAD, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param FILE_UPLOAD: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then FILE_UPLOAD is used
    :return: True if file was uploaded, else False
    """

    # Se object_name do S3 não foi especificado, use FILE_UPLOAD
    if object_name is None:
        object_name = os.path.basename(FILE_UPLOAD)

    # Upload do Arquivo
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(FILE_UPLOAD, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Upload DO ARQUIVO PARA O BUCKET no s3
s3 = boto3.client('s3')
with open(Arquivo_UPLOAD, "rb") as f:
    s3.upload_fileobj(f, BUCKET_NAME, "UploadExtrato2023Mod")
