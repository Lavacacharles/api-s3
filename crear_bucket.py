import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False
    return True
def lambda_handler(event, context):
    # Entrada

    nombre_bucket = event['body']['bucket']
    if create_bucket(nombre_bucket):
        return {
            'statusCode': 200,
            'nuevo_bucket': nombre_bucket
        }

# Cambia 'my-new-bucket-name' por el nombre de tu bucket y 'us-west-2' por tu región

