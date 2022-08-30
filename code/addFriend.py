import json
import boto3
import os
# import requests

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['tableName'])


def lambda_handler(event, context):
    message = json.loads(event['body'])
    print(message)
    response = table.put_item(
        Item=message
    )
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Friend added"
            }
        ),
    }
