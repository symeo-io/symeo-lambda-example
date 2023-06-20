import boto3


class AwsClient:
    def __init__(
        self,
        aws_access_key_id: str,
        aws_secret_access_key: str,
    ):
        self.__aws_access_key_id = aws_access_key_id
        self.__aws_secret_access_key = aws_secret_access_key

    def get_client(self):
        return boto3.client(
            "s3",
            # aws_access_key_id=self.__aws_access_key_id,
            # aws_secret_access_key=self.__aws_secret_access_key,
        )
