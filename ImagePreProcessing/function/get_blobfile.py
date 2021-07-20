from azure.storage.blob import BlobServiceClient, BlobClient, __version__
import logging
import os

def downLoadFile(container_client):
    logging.info("Azure Blob Storage v" + __version__)

    connect_blob = "fY8lq3DMilBGVu09YgSxE3V9uajAS8LUhJIqviqY0n8s2wtZa9cLsns8IiVXv+5ym2t1WAeffoBeOsjyKry89A=="

    blob_service_client = BlobServiceClient.from_connection_string(connect_blob)

    # 実際はログイン情報をもとにコンテナを参照する
    container_name = "techc"

    container_client = blob_service_client.container

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print('\t' + blob.name)

    xlx_filename

    return xlx_filename
