from pydantic import BaseModel


class BaseAppErrorModel(BaseModel):
    message: str
