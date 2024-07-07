import boto3
from botocore.exceptions import ClientError

def create_directory(bucket_name, directory_name):
    """
    Crea un "directorio" en un bucket de S3 subiendo un objeto vacío con una barra al final
    
    :param bucket_name: Nombre del bucket de S3
    :param directory_name: Nombre del "directorio" a crear
    :return: True si el "directorio" fue creado, de lo contrario False
    """
    # Asegúrate de que el nombre del directorio termine en '/'
    if not directory_name.endswith('/'):
        directory_name += '/'

    # Crea el "directorio" (objeto vacío con el nombre del directorio)
    s3_client = boto3.client('s3')
    try:
        s3_client.put_object(Bucket=bucket_name, Key=directory_name)
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False
    return True

def lambda_handler(event, context):
    # Entrada
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directory']
    if create_directory(nombre_bucket, nombre_directorio):
        return {
            'statusCode': 200,
            'nuevo_bucket': nombre_bucket
        }

