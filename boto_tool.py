import boto3

def latestVpcNatImageId(region='us-west-1'):
    client = boto3.client('ec2', region_name=region)
    images = client.describe_images(
        Owners=['amazon'],
        Filters=[
            {
                "Name":"name",
                "Values":['*vpc-nat*']},
            {
                "Name":"virtualization-type",
                "Values":['hvm']},
            {
                "Name":"root-device-type",
                "Values":['ebs']}])

    latest = ''
    for item in images['Images']:
        if latest < item['CreationDate']:
            latest = item['CreationDate']
            ami = item['ImageId']
        
    return ami
