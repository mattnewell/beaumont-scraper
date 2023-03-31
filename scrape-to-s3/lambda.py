import json
import boto3

sqs = boto3.client('sqs')

def handler(event, context):
    message = f'Hello, foo, {event}'
    return {
        'message': message
    }