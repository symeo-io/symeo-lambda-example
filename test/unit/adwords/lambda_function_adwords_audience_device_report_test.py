import unittest
from pathlib import Path

import pandas as pd

from src.application.lambda_processor import LambdaProcessor
from src.domain.default_raw_to_clean_processor import DefaultRawToCleanProcessor
from src.infrastructure.cleaner.adwords.adwords_audience_cleaner_adapter import (
    AdwordsAudienceCleanerAdapter,
)
from src.infrastructure.transformer.parquet_transformer_adapter import (
    ParquetTransformerAdapter,
)
from test.unit.mock.mocks import InputDataReaderMock, OutputDataWriterMock
from test.unit.s3_stub_utils import S3StubUtils


class LambdaFunctionAdwordsAudienceDeviceReportTest(unittest.TestCase):
    def test_should_process_clean_transform_json_to_parquet(self):
        json_name = "Europe_Paris.fr-FR.EUR.2022-01-17.gads-report-gender.1316752390.json"
        event = S3StubUtils.build_event(json_name, "dummy-source-bucket-name")
        target_bucket = "dummy-target-bucket-name"
        df_to_return = self.__read_json_from_resources(json_name)
        input_data_reader_mock = InputDataReaderMock(df_to_return)
        output_data_writer_mock = OutputDataWriterMock()
        adwords_audience_cleaner_adapter = AdwordsAudienceCleanerAdapter()
        parquet_transformer_adapter = ParquetTransformerAdapter()
        default_raw_to_clean_processor = DefaultRawToCleanProcessor(
            input_data_reader_mock,
            adwords_audience_cleaner_adapter,
            parquet_transformer_adapter,
            output_data_writer_mock,
        )

        dv360_raw_to_clean_lambda_processor = LambdaProcessor(default_raw_to_clean_processor)

        dv360_raw_to_clean_lambda_processor.process_event(event, target_bucket)
        self.assertEquals(1, output_data_writer_mock.get_number_of_write())

    def __read_json_from_resources(self, json_name: str) -> pd.DataFrame:
        adwords_json_test_directory = Path(__file__).parent.parent.parent / Path("./resources/adwords")
        return pd.read_json(adwords_json_test_directory.as_posix() + "/" + json_name)
