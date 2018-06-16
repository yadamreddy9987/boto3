import boto3
import json
import sys
import argparse

def init():
    return boto3.Session()

def detail_instance(region, instance_id):
    sess = init()
    ct_conn     = sess.client(service_name='cloudtrail',region_name=region)
    events_dict = ct_conn.lookup_events(LookupAttributes=[{'AttributeKey':'ResourceName', 'AttributeValue':instance_id}])
    for data in events_dict['Events']:
        json_file= json.loads(data['CloudTrailEvent'])
        print (json_file['userIdentity']['userName'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--list', nargs='+', help='Run <script name> -l <region> <instance_id>', required=True)
    args = parser.parse_args()
    region=args.list[0]
    instance_id=args.list[1]
    detail_instance(region, instance_id)

