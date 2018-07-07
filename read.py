import boto3


s3 = boto3.resource('s3')

my_bucket = s3.Bucket('practice-test1')

for objects in my_bucket.objects.all():
    print(objects.key)
