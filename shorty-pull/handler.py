import os
import json
import boto3

ddb = boto3.resource("dynamodb", region_name="us-west-2").Table("shorty-table")
hostname = os.getenv("BASE_URL")


def lambda_handler(event, context):
    print(event)
    short_url_id = event.get("pathParameters").get("short_url_id")
    print(short_url_id)

    try:
        item = ddb.get_item(Key={"short_url_id": short_url_id})
        original_url = item.get("Item").get("original_url")
        print("Original URL is: " + original_url)

    except:
        response = {
            "statusCode": 301,
            "headers": {
                "Location": hostname,
            },
        }
        return response

    response = {
        "statusCode": 301,
        "headers": {
            "Location": original_url,
        },
    }
    return response
