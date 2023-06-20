import pandas

from src.domain.port.model.target_object import TargetObject
from src.domain.port.obtain.obtain_input_data_cleaner_adapter import (
    ObtainInputDataCleanerAdapter,
)
from src.domain.port.obtain.obtain_input_data_reader_adapter import (
    ObtainInputDataReaderAdapter,
)
from src.domain.port.obtain.obtain_output_data_transformer_adapter import (
    ObtainOutputDataTransformerAdapter,
)
from src.domain.port.obtain.obtain_output_data_writer_adapter import (
    ObtainOutputDataWriterAdapter,
)


class InputDataReaderMock(ObtainInputDataReaderAdapter):
    __number_of_read = 0

    def __init__(self, df_to_return: pandas.DataFrame):
        self.__df_to_return = df_to_return

    def read(self, input_parameters: dict) -> pandas.DataFrame:
        self.__number_of_read += 1
        return self.__df_to_return

    def get_number_of_read(self):
        return self.__number_of_read


class InputDataCleanerMock(ObtainInputDataCleanerAdapter):
    __number_of_clean = 0

    def clean(self, input_data_to_clean: pandas.DataFrame) -> pandas.DataFrame:
        self.__number_of_clean += 1
        return input_data_to_clean

    def get_number_of_clean(self):
        return self.__number_of_clean


class OutputDataTransformerMock(ObtainOutputDataTransformerAdapter):
    __number_of_transform = 0

    def transform(self, input_data: pandas.DataFrame) -> pandas.DataFrame:
        self.__number_of_transform += 1
        return input_data

    def get_number_of_transform(self):
        return self.__number_of_transform


class OutputDataWriterMock(ObtainOutputDataWriterAdapter):
    __number_of_write = 0

    def write(self, input_data: pandas.DataFrame, target_object: TargetObject) -> None:
        self.__number_of_write += 1

    def get_number_of_write(self):
        return self.__number_of_write
