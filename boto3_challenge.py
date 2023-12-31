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


input("Visit your console to verify the existing buckets, then press enter to continue")

    
create_bucket('boto3challenge', 'us-west-2')

# Output the bucket names after bucket creation
s3 = boto3.client('s3')
response = s3.list_buckets()
print('Existing buckets after creating:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

input("Visit your console to verify the bucket creation, then press enter to continue")

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
    os.system(f"wget -O Homero_La_Iliada.txt {url}")
    print('Book was downloaded successfully!.')


download_book()


upload_file('Homero_La_Iliada.txt', 'boto3challenge')

input("Visit your console to verify that file was uploaded, then press enter to continue")

# Reading and printing txt file on S3 bucket
def print_file():
    response = s3.list_objects_v2(Bucket='boto3challenge')
    for item in response['Contents']:
        print(item['Key'])


print_file()

input("See your terminal to verify that the file was listed, then press enter to continue")


def read_file():
    response = s3.get_object(
        Bucket='boto3challenge',
        Key='Homero_La_Iliada.txt'
        )
    contents = response['Body'].read()
    # print(f'Reading the file {response.Key}')
    print(contents.decode("utf-8"))

    

read_file()

input("See your terminal to verify the file was readed, then press enter to continue")


def delete_file():
    response = s3.delete_object(
        Bucket='boto3challenge',
        Key='Homero_La_Iliada.txt'
        )
    print(response)
    print('-----')
    print(f'File deleted succesfully!.')
    

delete_file()

input("Visit your console to verify the file was removed, then press enter to continue")


def delete_bucket():
    response = s3.delete_bucket(
        Bucket='boto3challenge',
        )
    print(response)
    print('-----')
    print(f'Bucket deleted successfully!.')


delete_bucket()



def delete_downloaded_book():
    os.system(f'rm Homero_La_Iliada.txt')
    print('Downloaded book was removed from local.')


delete_downloaded_book()

input("Visit your console to verify the existing bucket was removed, then press enter to continue")

print('Script was executed successfully!.')