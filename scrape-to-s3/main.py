import boto3
from smart_open import open

input_file = 'https://www.beaumont.org/docs/default-source/default-document-library/cdm-documents/2023/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'
s3_file = 's3://paylesshealth/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'


def upload_to_s3():
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


def insert_queue():
    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-2.amazonaws.com/566613373177/paylesshealth-main'
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=input_file
    )
    print(response)


if __name__ == '__main__':
    # upload_to_s3()
    insert_queue()
