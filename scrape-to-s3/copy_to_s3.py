import os
import json
from smart_open import open


def upload_to_s3(data):
    enrollment_id = data['enrollment_id']
    url = data['url']
    print(url)
    s3_file = f's3://paylesshealth/{enrollment_id}/{os.path.basename(url)}'
    with open(url, 'r', encoding='iso-8859-1') as src:
        with open(s3_file, 'w', encoding='utf-8') as dest:
            dest.write(src.read())


def handler(event, context):
    print(json.dumps(event))
    for record in event['Records']:
        body = json.loads(record['body'])
        url = body['url']
        upload_to_s3(body)
