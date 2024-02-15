from pydantic import BaseModel


class ConfigurationModel(BaseModel):
    data_path: str = './data'
    purge_contents: bool = True
    replace_names: bool = False
    save_compact: bool = False


class SetupSuccessRespose(BaseModel):
    data_owner: str
    path_to_compact: str


class IsDataLoadedResponse(BaseModel):
    is_data_loaded: bool
