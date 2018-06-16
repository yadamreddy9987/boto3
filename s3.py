import boto3
def init_client():
    return boto3.client('s3')

def init_resource():
    return boto3.resource('s3')

def check_empty_bucket():
    s3client = init_client()
    s3resource = init_resource()
    for bucket in s3resource.buckets.all():
        print (bucket.name)
        try:
            number_object=s3client.list_objects(Bucket=bucket.name)['Contents'].len()
        except:
            print ("bucket", bucket.name, "is empty")

if __name__ == "__main__":
    check_empty_bucket()
