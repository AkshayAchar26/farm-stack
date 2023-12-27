from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    origins:str
    mongo_url:str
    
    model_config = SettingsConfigDict(env_file=".env",env_file_encoding='utf-8')
    

@lru_cache  
def get_settings() -> Settings:
    print('started')
    return Settings()
    