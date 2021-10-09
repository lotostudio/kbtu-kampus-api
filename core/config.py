from typing import List, Union

from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):

    PROJECT_NAME: str = 'KBTU Kampus API'
    SECRET_KEY: str

    VERSION: str = '0.0.1'

    ACCESS_TOKEN_EXPIRATION: int

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @classmethod
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    POSTGRADUATE_PORTAL_URL: str

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
