import boto3

## Using Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload new file
data = open('/Users/siyunhe/project/Yolominds-Team/AWS-S3-Upload/test_aws_spacex.png', 'rb')
s3.Bucket('test-somercloud-s3-image-upload-bucket1').put_object(Key='test_aws_spacex.png', Body=data)



    
    
