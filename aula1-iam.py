import boto3


iam_client = boto3.client("iam")

for user in iam_client.list_users()["Users"]:
    print(user["UserName"])
