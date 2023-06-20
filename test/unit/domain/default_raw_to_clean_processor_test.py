import unittest

from pandas import DataFrame as df

from src.domain.default_raw_to_clean_processor import DefaultRawToCleanProcessor
from test.unit.mock.mocks import (
    InputDataReaderMock,
    InputDataCleanerMock,
    OutputDataTransformerMock,
    OutputDataWriterMock,
)


class DefaultRawToCleanProcessorTest(unittest.TestCase):
    def test_should_process_data_from_raw_storage_to_clean_storage(self):
        # Given
        input_data_stub = df.from_dict({})
        obtain_input_data_reader_mock = InputDataReaderMock(input_data_stub)
        obtain_input_data_cleaner_mock = InputDataCleanerMock()
        obtain_output_data_transformer_mock = OutputDataTransformerMock()
        obtain_output_data_writer_mock = OutputDataWriterMock()
        input_parameters = {}
        raw_to_clean_processor = DefaultRawToCleanProcessor(
            obtain_input_data_reader_mock,
            obtain_input_data_cleaner_mock,
            obtain_output_data_transformer_mock,
            obtain_output_data_writer_mock,
        )

        # When
        raw_to_clean_processor.process(input_parameters)

        # Then
        self.assertEquals(1, obtain_input_data_reader_mock.get_number_of_read())
        self.assertEquals(1, obtain_input_data_cleaner_mock.get_number_of_clean())
        self.assertEquals(
            1, obtain_output_data_transformer_mock.get_number_of_transform()
        )
        self.assertEquals(1, obtain_output_data_writer_mock.get_number_of_write())
