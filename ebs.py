import boto3
def init(region):
    return boto3.resource('ec2', region)

def init_client(region):
    return boto3.client(service_name='cloudtrail',region_name=region)

def remove_unused_vol():
    regions={"ap-south-1","eu-west-3","eu-west-2","eu-west-1","ap-northeast-2","ap-northeast-1","sa-east-1","ca-central-1","ap-southeast-1","ap-southeast-2","eu-central-1","us-east-1","us-east-2","us-west-1","us-west-2"}
    for region in regions:
        ec2resources = init(region) 
        for vol in ec2resources.volumes.all():
            if vol.state=='available':
                  print (region,",", vol.state,",", vol.id,",", vol.size,"GB,", vol.create_time)
                  #print (region, vol, vol.state)
                  #unattached_volume=ec2resources.Volume(vol.id)
                  #unattached_volume.delete()
                  #print "Deleted " + unattached_volume

if __name__ == "__main__":
    remove_unused_vol()
