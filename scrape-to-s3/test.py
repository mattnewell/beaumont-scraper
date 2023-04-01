import copy_to_s3
import json

with open('event.json', 'r') as file:
    event = json.loads(file.read())

copy_to_s3.handler(event, None)
