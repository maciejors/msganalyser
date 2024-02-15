from pydantic import BaseModel


class ConfigurationModel(BaseModel):
    data_path: str = './data'
    purge_contents: bool = True
    replace_names: bool = False


class DataOwnerResponse(BaseModel):
    data_owner: str


class IsDataLoadedResponse(BaseModel):
    is_data_loaded: bool
