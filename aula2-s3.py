from pprint import pprint
from uuid import uuid4
import boto3


s3_client = boto3.client("s3", region_name="us-east-2")


# nome_do_bucket = "meu-primeiro-baldinho" + str(uuid4())
# # Criando um bucket
# s3_client.create_bucket(
#     Bucket=nome_do_bucket, CreateBucketConfiguration={"LocationConstraint": "us-east-2"}
# )

s3_client.delete_bucket(
    Bucket="meu-primeiro-baldinhoe7a51933-62e5-4169-900b-630ed1131492"
)

response = s3_client.list_buckets()
# Listando os buckets existentes
print("Listando buckets:")
for bucket in response["Buckets"]:
    pprint(f'  {bucket["Name"]}')
