from smart_open import open

input_file = 'https://www.beaumont.org/docs/default-source/default-document-library/cdm-documents/2023/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'
s3_file = 's3://paylesshealth/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'


def upload_to_s3():
    # NOTE: I think the smart_open default is 50 MiB. Should probably align.
    chunk_size = 20 * 1024 * 1024  # 20 MiB
    with open(input_file, mode='rb') as fin:
        with open(s3_file, 'wb') as fout:
            while True:
                buffer = fin.read(chunk_size)
                if not buffer:
                    break
                fout.write(buffer)


if __name__ == '__main__':
    upload_to_s3()