from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    access_token: str
    app_id: str
    app_secret: str
    recipient_wa: str
    version: str
    phone_number_id: str
    verify_token: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
