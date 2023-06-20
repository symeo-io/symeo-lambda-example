from dataclasses import dataclass

from src.domain.port.model.source_object import SourceObject
from src.domain.port.model.target_object import TargetObject


@dataclass
class BucketObject(SourceObject, TargetObject):
    bucket: str
    key: str
