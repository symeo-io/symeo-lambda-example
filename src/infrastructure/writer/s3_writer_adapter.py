import logging
from src.domain.port.model.bucket_object import BucketObject
from src.domain.port.obtain.obtain_output_data_writer_adapter import (
    ObtainOutputDataWriterAdapter,
)
from src.infrastructure.client.aws_client import AwsClient

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class S3WriterParquetAdapter(ObtainOutputDataWriterAdapter):
    def __init__(self, aws_client: AwsClient):
        self.__aws_client = aws_client

    def write(self, bytes_to_write: bytes, target_bucket_object: BucketObject) -> None:
        LOGGER.info("Destination bucket: " + target_bucket_object.bucket)
        LOGGER.info("Destination prefix: " + target_bucket_object.key)
        s3_client = self.__aws_client.get_client()
        s3_client.put_object(
            Body=bytes_to_write,
            Key=target_bucket_object.key,
            Bucket=target_bucket_object.bucket,
        )
