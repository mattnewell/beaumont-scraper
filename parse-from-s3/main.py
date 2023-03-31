import polars as pl
import s3fs

input_file = 'https://www.beaumont.org/docs/default-source/default-document-library/cdm-documents/2023/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'
s3_file = 's3://paylesshealth/381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv'


def parse_from_s3():
    # fs = s3fs.S3FileSystem()
    # dataset = pl.read_csv(s3_file)
    df = pl.read_csv('381405141_beaumont-hospital-dearborn-hospital_standardcharges.csv')
    # output = df.melt(
    #     id_vars=[' Code Type', 'Procedure ', 'Code', ' NDC ', 'Rev Code ', 'Procedure Description', '  GROSS CHARGE   ',
    #              '  DE-IDENTIFIED  MINIMUM   ', '  DE-IDENTIFIED MAXIMUM    ', ' CASH PRICE '], variable_name='plan',
    #     value_name='price')
    output = df.select(
        pl.col(' Code Type'),
        pl.col('Code'),
        pl.lit('none')
    )
    output.head(100).write_csv('melted.csv')


if __name__ == '__main__':
    parse_from_s3()
