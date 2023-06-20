import pandas

from src.domain.port.model.source_object import SourceObject


class ObtainInputDataReaderAdapter:
    def read(self, source_object: SourceObject) -> pandas.DataFrame:
        pass
