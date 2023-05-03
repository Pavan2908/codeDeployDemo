import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! I am deployed from github! I am 2nd of my kind * 1')
    }
