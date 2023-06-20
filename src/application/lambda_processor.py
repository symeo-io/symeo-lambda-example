import json
import logging
import os

from src.domain.port.model.bucket_object import BucketObject
from src.domain.port.request.request_raw_to_clean_processor_adapter import (
    RequestRawToCleanProcessorAdaptor,
)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class LambdaProcessor:
    def __init__(self, raw_to_clean_processor: RequestRawToCleanProcessorAdaptor):
        self.__raw_to_clean_processor = raw_to_clean_processor

    def process_event(self, event, target_bucket_name):
        records = event["Records"]
        if len(records) != 1:
            """
            Rappel 1 : Sur un trigger SQS to Lambda. Si la lambda succeed, le message sqs est traite
                       et supprime de la file sqs.
                       Si la lambda echoue, au bout du n retry configure dans la sqs source, le message
                       est supprime de la file sqs pour etre poster dans la file sqs dlq.
            Rappel 2 : dans une lambda event triggered par sqs avec batch size superieur de 1
            Si la lambda echoue, tous les messages du batch sont repostés dans la sqs pour retry
            Même si certains n'ont pas pausé de problemes.
            Il est ainsi recommande d'avoir un batch size de 1 pour laisser SQS/DLQ gerer
            la stratégie sqs plutot que de le faire programmatiquement.
            """
            raise "this lambda handles only sqs triggers with batch size 1"

        input_event = json.loads(records[0]["body"])  # Permit car batch size = 1.
        key = input_event["detail"]["requestParameters"]["key"]
        bucket_source = input_event["detail"]["requestParameters"]["bucketName"]
        LOGGER.info("Source bucket: " + bucket_source)
        LOGGER.info("Source prefix: " + key)
        source_bucket_object = BucketObject(bucket_source, key)
        target_bucket_object = BucketObject(target_bucket_name, key.replace(".json", ".parquet"))
        self.__raw_to_clean_processor.process(source_bucket_object, target_bucket_object)

    @staticmethod
    def check_and_get_environment_variables():
        aws_access_key_id = LambdaProcessor.__check_and_return_environment_variable("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = LambdaProcessor.__check_and_return_environment_variable("AWS_SECRET_ACCESS_KEY")
        target_bucket = LambdaProcessor.__check_and_return_environment_variable("TARGET_BUCKET")
        return aws_access_key_id, aws_secret_access_key, target_bucket

    @staticmethod
    def __check_and_return_environment_variable(environment_variable: str) -> str:
        os_getenv = os.getenv(environment_variable)
        if os_getenv is None:
            raise Exception(f"Missing mandatory env variable {environment_variable}")
        return os_getenv
