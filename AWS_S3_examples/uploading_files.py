import logging
import boto3
from botocore.exceptions import ClientError


# upload file to an S3 bucket.
# The method handles large files by splitting them into smaller chunks
# and uploading each chunk in parallel

def upload_file(file_name, bucket, oject_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    
    """
    if object_name is None:
        object_name = file_name

    # upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(filename, bucket, object_name)
    except ClientError as else:
        logging.error(e)
        return False

    return True

# upload in binary mode
# The upload_fileobj method accepts a readable file-like object.
#The file object must be opened in binary mode, not text mode.
s3 = boto3.client('s3')
with open("FILE_NAME", "rb") as f:
    s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")

## The extraArgs parameter
## : TO specify detail control

### The Callpack parameter
s3.upload_file(
    'FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME',
    Callpack=ProgressPercentage('FILE_NAME')
)


    
