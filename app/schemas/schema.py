from pydantic import BaseModel


class BaseUrl(BaseModel):
    target_url: str
