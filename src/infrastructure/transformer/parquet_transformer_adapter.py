import pandas

from src.domain.port.obtain.obtain_output_data_transformer_adapter import (
    ObtainOutputDataTransformerAdapter,
)


class ParquetTransformerAdapter(ObtainOutputDataTransformerAdapter):
    def transform(self, input_data: pandas.DataFrame) -> bytes:
        return input_data.to_parquet()
