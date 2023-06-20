import logging

from src.application.lambda_processor import LambdaProcessor
from src.domain.default_raw_to_clean_processor import DefaultRawToCleanProcessor
from src.infrastructure.cleaner.adwords.adwords_audience_cleaner_adapter import (
    AdwordsAudienceCleanerAdapter,
)
from src.infrastructure.client.aws_client import AwsClient
from src.infrastructure.reader.s3_json_reader_adapter import S3JsonReaderAdapter
from src.infrastructure.transformer.parquet_transformer_adapter import (
    ParquetTransformerAdapter,
)
from src.infrastructure.writer.s3_writer_adapter import S3WriterParquetAdapter

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    LOGGER.info(f"Starting lambda for event {event} and context {context}")
    (
        aws_access_key_id,
        aws_secret_access_key,
        target_bucket,
    ) = LambdaProcessor.check_and_get_environment_variables()

    aws_client = AwsClient(
        aws_access_key_id,
        aws_secret_access_key,
    )
    default_raw_to_clean_processor = DefaultRawToCleanProcessor(
        S3JsonReaderAdapter(aws_client),
        AdwordsAudienceCleanerAdapter(),
        ParquetTransformerAdapter(),
        S3WriterParquetAdapter(aws_client),
    )
    dv360_raw_to_clean_lambda_processor = LambdaProcessor(
        default_raw_to_clean_processor
    )
    dv360_raw_to_clean_lambda_processor.process_event(event, target_bucket)
    LOGGER.info(f"End of lambda for event {event} and context {context}")
