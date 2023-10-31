# Importing the required libraries
import boto3
import logging
from botocore.exceptions import ClientError
import os


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets before creating:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
    
    
create_bucket('boto3challenge', 'us-west-2')

# Output the bucket names after bucket creation
print('Existing buckets after creating:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# Uploading files
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# Downloading Homero - La Iliada book
def download_book():
    url = 'https://www.gutenberg.org/cache/epub/57654/pg57654.txt'
    os.system(f"wget -O Homero_La_Iliada.tx {url}")
    
    
upload_file('Homero_La_Iliada.txt', 'boto3challenge')

# Reading and printing txt file on S3 bucket


# aws s3 cp s3://boto3challenge/Homero_La_Iliada.txt - | head -100

# Delete objetc in s3
# aws s3 rm s3://boto3challenge/Homero_La_Iliada.txt

# Delete bucket
# aws s3 rb boto3challenge