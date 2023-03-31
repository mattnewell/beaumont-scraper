import json

import boto3
from smart_open import open

s3_file = 's3://paylesshealth/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'


def upload_to_s3(input_file):
    # NOTE: I think the smart_open default is 50 MiB. Should probably align.
    # chunk_size = 20 * 1024 * 1024  # 20 MiB
    # with open(input_file, mode='rb') as fin:
    #     with open(s3_file, 'wb') as fout:
    #         while True:
    #             buffer = fin.read(chunk_size)
    #             if not buffer:
    #                 break
    #             fout.write(buffer)
    with open(input_file, 'r', encoding='iso-8859-1') as src:
        with open(s3_file, 'w', encoding='utf-8') as dest:
            dest.write(src.read())


def handler(event, context):
    upload_to_s3(event.get('uri'))
