import json
import os
from fabric.operations import sudo


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    a = os.getenv("TEST")
    b = os.environ["TEST"]
    c = os.environ.get("TEST")
    d = os.open("TEST")

    cmd = os.getenv("TEST")

    g = event["Hello"]

    os.system(a)

    f = sudo(a)  # <-- add 'cmd' as a taint sink

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
