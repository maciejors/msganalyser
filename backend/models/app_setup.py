from pydantic import BaseModel


class ConfigurationModel(BaseModel):
    data_path: str
