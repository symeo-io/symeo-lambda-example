import pandas

from src.domain.port.model.target_object import TargetObject


class ObtainOutputDataWriterAdapter:
    def write(self, bytes_to_write: bytes, target_object: TargetObject) -> None:
        pass
