import io

import pandas as pd

from src.domain.port.model.bucket_object import BucketObject
from src.domain.port.obtain.obtain_input_data_reader_adapter import (
    ObtainInputDataReaderAdapter,
)
from src.infrastructure.client.aws_client import AwsClient


class S3CsvReaderAdapter(ObtainInputDataReaderAdapter):
    def __init__(self, aws_client: AwsClient):
        self.__aws_client = aws_client

    def read(self, source_bucket_object: BucketObject) -> pd.DataFrame:
        s3_client = self.__aws_client.get_client()
        obj = s3_client.get_object(
            Bucket=source_bucket_object.bucket,
            Key=source_bucket_object.key,
        )
        df = pd.read_csv(io.BytesIO(obj["Body"].read()))
        return df
