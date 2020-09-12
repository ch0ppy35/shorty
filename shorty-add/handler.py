import os
import json
import boto3
import datetime
from math import floor
from string import ascii_lowercase, ascii_uppercase, digits


hostname = os.getenv("BASE_URL")
app_url = os.getenv("APP_URL")
ddb = boto3.resource("dynamodb", region_name="us-west-2").Table("shorty-table")


def to_base_62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = digits + ascii_lowercase + ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res


def generate_url_id():
    seconds_since_epoch = datetime.datetime.now().timestamp()
    seconds_since_epoch = int(seconds_since_epoch)
    short_url_id = to_base_62(seconds_since_epoch)
    print("The short_url_id is: " + short_url_id)
    response = short_url_id
    return response


def lambda_handler(event, context):
    print(event)
    short_url_id = generate_url_id()
    short_url = app_url + short_url_id
    original_url = json.loads(event.get("body")).get("original_url")

    response = ddb.put_item(
        Item={
            "short_url_id": short_url_id,
            "short_url": short_url,
            "original_url": original_url,
        }
    )

    return {"statusCode": 200, "body": short_url}
