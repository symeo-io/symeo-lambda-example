import pandas

from src.domain.port.obtain.obtain_input_data_cleaner_adapter import (
    ObtainInputDataCleanerAdapter,
)


class AdwordsAudienceCleanerAdapter(ObtainInputDataCleanerAdapter):
    def clean(self, input_data_to_clean: pandas.DataFrame) -> pandas.DataFrame:
        return input_data_to_clean
