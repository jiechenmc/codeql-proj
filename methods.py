import boto3

client = boto3.client("s3")
operations = client.meta.service_model.operation_names
print(operations)
