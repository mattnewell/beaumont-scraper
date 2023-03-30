import polars as pl
import s3fs

input_file = 'https://www.beaumont.org/docs/default-source/default-document-library/cdm-documents/2023/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'
s3_file = 's3://paylesshealth/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'


def parse_from_s3():
    fs = s3fs.S3FileSystem()
    dataset = pl.read_csv(s3_file)


if __name__ == '__main__':
    parse_from_s3()
