import os, uuid
from azure.storage.blob import BlobClient, BlobServiceClient, __version__, download_blob_from_url

try:
    print("Azure Blob Storage v" + __version__)

    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    container_name = str(uuid.uuid4())

    container_client = blob_service_client.create_container(container_name)

    local_path = "./data"
    os.mkdir(local_path)

    local_file_name = str(uuid.uuid4()) + '.txt'
    upload_file_path = os.path.join(local_path, local_file_name)

    file = open(upload_file_path, 'w')
    file.write("Hello World")
    file.close()

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob: \n\t" + local_file_name)

    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

    print("\nListing blobs...")

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print('\t' + blob.name)

    download_file_path = os.path.join(local_path, str.replace(local_file_name, '.txt', 'DOWNLOAD.txt'))
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    print("\nPress the Enter key to begin clean up")
    input()

    print("Deleting blob container...")
    container_client.delete_container()

    print("Deleting the local source and downloaded files...")
    os.remove(upload_file_path)
    os.remove(download_file_path)
    os.remove(local_path)
    
    print("Done")

    

except Exception as e:
    print('Exception:')
    print(e)