import boto3
from pprint import pprint


# open ec2 console
ec2_client = boto3.client(service_name="ec2", region_name="us-east-2")

result = ec2_client.describe_instances()

pprint(result)

# criando sua primeira instância no ec2
response = ec2_client.run_instances(
    ImageId="ami-019f9b3318b7155c5",
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1,
)

pprint(response)

# como parar as instancias
# response = ec2_client.stop_instances(
#     InstanceIds=["i-0efb9edb10a518cc8"],
# )

# pprint(response)

# # como terminar as instancias
# response = ec2_client.terminate_instances(
#     InstanceIds=["i-0efb9edb10a518cc8"],
# )

# pprint(response)
