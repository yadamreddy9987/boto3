import boto3
import datetime

def init(resource, region):
    return boto3.client(resource, region_name=region)

def search_cloudwatch_matrix(cw, bucket_name, count_keys):
    now = datetime.datetime.now()
    response = cw.get_metric_statistics(Namespace='AWS/S3',
                                MetricName='BucketSizeBytes',
                                Dimensions=[
                                    {'Name': 'BucketName', 'Value': bucket_name},
                                     {'Name': 'StorageType', 'Value': 'StandardStorage'}
                                ],
                                Statistics=['Average'],
                                Period=3600,
                                StartTime=(now-datetime.timedelta(days=1)).isoformat(),
                                EndTime=now.isoformat()
                                )
    for item in response["Datapoints"]:
        print( bucket_name.ljust(45) + str("{:,}".format(int(item["Average"]))).rjust(25) + " ".rjust(25), count_keys )
    
def get_bucket_detail():
    s3client = boto3.client('s3')
    allbuckets = s3client.list_buckets()
    print('Bucket'.ljust(45) + 'Size in Bytes'.rjust(25) + "count".rjust(25))
    #regions={"ap-south-1","eu-west-3","eu-west-2","eu-west-1","ap-northeast-2","ap-northeast-1","sa-east-1","ca-central-1","ap-southeast-1","ap-southeast-2","eu-central-1","us-east-1","us-east-2","us-west-1","us-west-2"}
    regions={"eu-west-1"}
    for region in regions:
        cw = init('cloudwatch', region)
        for bucket in allbuckets['Buckets']:
            #print (bucket['Name'])
            try:
                count_keys = len(s3client.list_objects(Bucket=bucket['Name'])['Contents'])
            except:
                print (bucket['Name'] + "object does not exist...empty bucket")
            search_cloudwatch_matrix(cw, bucket['Name'], count_keys)

if __name__ == "__main__":
    get_bucket_detail()
