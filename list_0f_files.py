import boto3


s3 = boto3.resource('s3')
my_bucket = s3.Bucket('practice-test1')
list_file=[]
print(type(list_file))
for objects in my_bucket.objects.all():
    print(list_file.append(objects.key))


