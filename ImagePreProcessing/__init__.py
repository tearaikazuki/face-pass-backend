from azure.storage.blob import BlobClient, BlobServiceClient
from openpyxl import load_workbook
from PIL import Image
import logging
import time
import glob
import grpc
import azure.functions as func

# IPADDRESS, PORT


def main(req: func.HttpRequest) -> func.HttpResponse:
    _NAME = 'image'

    event_id = context.invocation_id
    logging.info('Python HTTP trigger function processed a request.')

    try:
        method = req.method
        url = req.url
        files = req.files[_NAME]

        if method != 'POST':
            logging.warning(
                f'ID:{event_id},the method was {files.content_type}.refused.')
            return func.HttpResponse(f'only accept POST method', status_code=400)

        if files:
            if files.content_type != 'image/png':
                return func.HttpResponse(f'only accept png images.', status_code=400)

            # --- 画像の前処理 ---
            
            # 画像の読み込み

            # 画像サイズの変更(500x500)
            
            # 画像の保存

            # ---


            # --- 画像をモデルに送る ---


            # ---



            # --- Blobの処理 ---

            # 各Blobからスプレッドシートとタグリストを取得する(sheet=出欠簿, tag=タグリスト)
            
            # スプレッドシートの情報とタグを参照する(一致=status変更, 不一致=変更なし)

            # スプレッドシートの保存

            # 変更内容をBlobに反映させる

            # ---

        return func.HttpResponse()
    except grpc.RpcError as e:
        logging.error(e)
        return func.HttpResponse(f'the grpc request timeout', status_code=408)
    except Exception as e:
        logging.error(e)
        return func.HttpResponse(f'Service Error.check the log.', status_code=500)
