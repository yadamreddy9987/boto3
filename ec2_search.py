#!/usr/local/bin/python3
import boto3

def init():
    return boto3.Session()  

def print_instance_details(region,instanceId, instanceName, instanceType, LaunchTime):
    print (region, ",", instanceId, ",", instanceName, ",", instanceType, ",", LaunchTime)

def list_instances():
    session=init()
    regions={"ap-south-1","eu-west-3","eu-west-2","eu-west-1","ap-northeast-2","ap-northeast-1","sa-east-1","ca-central-1","ap-southeast-1","ap-southeast-2","eu-central-1","us-east-1","us-east-2","us-west-1","us-west-2"}
    for region in regions:
        ec2client = session.client('ec2',region_name=region)
        response=ec2client.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                counter=0
                flag=0
                try:
                    number_tags=len(instance["Tags"])
                    while(counter<number_tags):
                        if (instance["Tags"][counter]["Key"] == "Name"):
                            print_instance_details (region, instance["InstanceId"], instance["Tags"][counter]["Value"], instance["InstanceType"], instance["LaunchTime"])
                            flag=1
                            break
                        counter+=1
                    if (flag == 0):
                        raise Exception("call the exception to print the instance details")
                except:
                    number_tags=0
                    print_instance_details (region, instance["InstanceId"], "none", instance["InstanceType"], instance["LaunchTime"])

if __name__ == "__main__":
   list_instances()
