import boto3
import bs4
import os
from pathlib import Path

# client = boto3.client("s3")
# operations = client.meta.service_model.operation_names
# print(operations)

serverless_repo_location = "Serverless_Repositories"


def find_serverless_yaml(search_path: str, filename: str = "serverless.yml"):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


def analyze(folder_name: str):
    search_path = f"{serverless_repo_location}/{folder_name}"
    # print(search_path)
    # print(find_serverless_yaml(search_path))

    for p in Path(search_path).rglob("*.py"):  # Use "*.txt" for filtering
        print(p)


def main():
    folders = os.listdir(serverless_repo_location)
    for folder in folders:
        analyze(folder)


if __name__ == "__main__":
    main()
