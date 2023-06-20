class S3StubUtils:
    @staticmethod
    def build_event(bucket_key, bucket_name):
        return {
            "version": "0",
            "id": "1fc79f42-2559-89e4-a7a1-6c21ead172c3",
            "detail-type": "AWS API Call via CloudTrail",
            "source": "aws.s3",
            "account": "412265628846",
            "time": "2021-11-26T08:19:35Z",
            "region": "eu-west-1",
            "resources": [],
            "detail": {
                "requestParameters": {
                    "X-Amz-Date": "20211126T081935Z",
                    "bucketName": bucket_name,
                    "X-Amz-Algorithm": "AWS4-HMAC-SHA256",
                    "x-amz-acl": "private",
                    "X-Amz-SignedHeaders": "content-md5;content-type;host;x-amz-acl;x-amz-storage-class",
                    "Host": "symeo-aclet-dtlk-raw-dv360-daily-yln.s3.eu-west-1.amazonaws.com",
                    "X-Amz-Expires": "300",
                    "key": bucket_key,
                    "x-amz-storage-class": "STANDARD",
                },
            },
        }
