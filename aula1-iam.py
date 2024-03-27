import boto3

iam_client = boto3.client("iam")

for user in iam_client.list_users()["Users"]:
    print(user["UserName"])


# S3  => Simple Storage Service => S3
# EC2 => Elastic Compute Cloud => EC2