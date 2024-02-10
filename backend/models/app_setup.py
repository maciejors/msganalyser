from pydantic import BaseModel


class ConfigurationModel(BaseModel):
    data_path: str


class DataOwnerModel(BaseModel):
    data_owner: str
