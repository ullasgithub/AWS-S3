import boto3

# Create an S3 client
s3 = boto3.resource('s3')


my_bucket = s3.Bucket('practice-test1')

key_name = input("Enter File name : ")
for obj in my_bucket.objects.all():
    key = obj.key
    if key == key_name:
        body = obj.get()['Body'].read()
        print(body)
