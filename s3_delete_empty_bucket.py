import boto3
import argparse
def init_client():
    return boto3.client('s3')

def init_resource():
    return boto3.resource('s3')

def delete_bucket(s3client,bucket_name):
    print ("deleting the bucket:", bucket_name)
    # need to uncommnt the below line when we actually want to remove the bucket
    s3client.delete_bucket(Bucket=bucket_name)

def check_empty_bucket(DRYRUN):
    s3client = init_client()
    s3resource = init_resource()
    for bucket in s3resource.buckets.all():
        try:
            number_object=s3client.list_objects(Bucket=bucket.name)['Contents'][0]
        except:
            print ("bucket", bucket.name, "is empty")
            if ( DRYRUN == 'False' ):
                delete_bucket(s3client,bucket.name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dryrun', nargs='?', help='True or False [ For eg : <script> --dryrun True ]'  , default=True)
    arg = parser.parse_args()
    check_empty_bucket(arg.dryrun)
