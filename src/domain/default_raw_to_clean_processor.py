import logging
from src.domain.port.model.source_object import SourceObject
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
from src.domain.port.request.request_raw_to_clean_processor_adapter import (
    RequestRawToCleanProcessorAdaptor,
)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class DefaultRawToCleanProcessor(RequestRawToCleanProcessorAdaptor):
    def __init__(
        self,
        obtain_input_data_reader: ObtainInputDataReaderAdapter,
        obtain_input_data_cleaner: ObtainInputDataCleanerAdapter,
        obtain_output_data_transformer: ObtainOutputDataTransformerAdapter,
        obtain_output_data_writer: ObtainOutputDataWriterAdapter,
    ):
        self.__obtain_input_data_reader = obtain_input_data_reader
        self.__obtain_input_data_cleaner = obtain_input_data_cleaner
        self.__obtain_output_data_transformer = obtain_output_data_transformer
        self.__obtain_output_data_writer = obtain_output_data_writer

    def process(self, source_object: SourceObject, target_object: TargetObject):
        input_data = self.__obtain_input_data_reader.read(source_object)
        LOGGER.debug("input data len: %s" % len(input_data))
        cleaned_input_data = self.__obtain_input_data_cleaner.clean(input_data)
        LOGGER.debug("cleaned_input_data data len: %s" % len(cleaned_input_data))
        transformed_output_data = self.__obtain_output_data_transformer.transform(cleaned_input_data)
        LOGGER.debug("transformed data done")
        self.__obtain_output_data_writer.write(transformed_output_data, target_object)
        LOGGER.debug("write done")
