import boto3
import json
import mysql.connector


def list_urls():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        database='paylesshealth'
    )
    cursor = db.cursor()
    cursor.execute("SELECT enrollment_id, standard_charge_file_url FROM hospitals WHERE standard_charge_file_url like "
                   "'%standardcharges.csv'")
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return rows



def insert_queue(rows):
    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-2.amazonaws.com/566613373177/paylesshealth-main'
    for row in rows:
        data = {
            'enrollment_id': row[0],
            'url': row[1]
        }
        print(json.dumps(data))
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(data)
        )


if __name__ == '__main__':
    rows = list_urls()
    insert_queue(rows)
