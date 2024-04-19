"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3, ec2

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

ec2_instance = ec2.Instance("web-server",ami="ami-04f73ca9a4310089f",instance_type="t3.nano",key_name="generals-login",tags={
    "Name":"web server"
})
pulumi.export('public_ip', ec2_instance.public_ip)
