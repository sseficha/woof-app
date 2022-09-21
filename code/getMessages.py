import json
import boto3
import os
# import requests
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['tableName'])


def lambda_handler(event, context):
    user_email = event['queryStringParameters']['user_email']
    response = table.query(
        KeyConditionExpression=Key('user_email').eq(user_email)
    )
    print(response["Items"])
    return {
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "statusCode": 200,
        "body": json.dumps(
            response["Items"]
        ),
    }
