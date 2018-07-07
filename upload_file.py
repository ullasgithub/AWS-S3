import boto3

# Create an S3 client
s3 = boto3.client('s3')


bucket_name = 'practice-test1'

# Uploads the given file
with open("hello.txt", "rb") as f:
    s3.upload_fileobj(f, bucket_name, "hello")