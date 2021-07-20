from function import resize_img
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient, __version__
from openpyxl import load_workbook
import logging
import shutil
import time
import glob
import os, uuid
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
        img_files = req.files[_NAME]

        if method != 'POST':
            logging.warning(
                f'ID:{event_id},the method was {img_files.content_type}.refused.')
            return func.HttpResponse(f'only accept POST method', status_code=400)

        if img_files:
            if img_files.content_type != 'image/png':
                return func.HttpResponse(f'only accept png images.', status_code=400)

            # --- 画像の前処理 ---
            
            # 画像の読み込み
            img = img_files.read()
            # 画像サイズの変更(300x300), 画像を保存
            img_re = resize_img(img)
            # ---
            # --- 画像をモデルに送る ---


            # ---



            # --- Blobの処理 ---
            logging.info("Azure Blob Storage v" + __version__)
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