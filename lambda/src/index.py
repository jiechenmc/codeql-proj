import boto3
import os
from datetime import datetime

s3 = boto3.client("s3")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "your-default-bucket")


def main_handler(event, context):
    sc = os.getenv("TEST")
    file = open(sc)

    sc2 = os.environ["test"]
    file2 = open(sc2)

    sc3 = os.environ.get("test")
    file3 = open(sc3)

    db = {"Helo": "Word"}

    print(db["Helo"])

    # Sample file content
    content = "Hello from Lambda at {}".format(datetime.utcnow().isoformat())

    # Define the file name
    file_name = "uploads/hello_{}.txt".format(
        datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    )

    try:
        response = s3.put_object(
            Bucket=BUCKET_NAME, Key=file_name, Body=content.encode("utf-8")
        )
        return {
            "statusCode": 200,
            "body": f"File uploaded to s3://{BUCKET_NAME}/{file_name}",
        }
    except Exception as e:
        return {"statusCode": 500, "body": f"Failed to upload file: {str(e)}"}
