import json
import os
from fabric.operations import sudo
import boto3

import urllib3

from django.db import models

import urllib3

http = urllib3.PoolManager()
response = http.request("GET", "https://httpbin.org/get")
print(response.status)
print(response.data)

s3 = boto3.resource("s3")


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    a = os.getenv("TEST")
    b = os.environ["TEST"]
    c = os.environ.get("TEST")
    d = os.open("TEST")

    cmd = os.open(response.data)

    s3.table.put_item()

    cmd = os.getenv("TEST")

    g = event["Hello"]

    os.system(a)

    f = sudo(a)

    print(f)

    with open("TEST") as e:
        os.open(e)

    open(a)
    open(b)
    open(c)
    open(d)
    open(g)

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
