# import boto3
import boto3
from pprint import pprint


# open ec2 console
ec2_console = boto3.client(service_name="ec2")

result = ec2_console.describe_instances()

pprint(result)

# criando sua primeira instância no ec2
# response = ec2_console.run_instances(
#     ImageId="ami-07761f3ae34c4478d",
#     InstanceType="t2.micro",
#     MaxCount=1,
#     MinCount=1,
# )

# pprint(response)

# como parar as instancias
response = ec2_console.stop_instances(
    InstanceIds=["i-02d083fd3cfc17e4f"],
)

pprint(response)

# como terminar as instancias
response = ec2_console.terminate_instances(
    InstanceIds=["i-02d083fd3cfc17e4f"],
)

pprint(response)
