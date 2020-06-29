from pathlib import Path
import os
from dotenv import load_dotenv


class Config:
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    django_key = os.getenv('django_key')
    DEBUG = os.getenv('DEBUG')
    aws_s3_access_key_id = os.getenv('aws_s3_access_key_id')
    aws_s3_secret_access_key = os.getenv('aws_s3_secret_access_key')
    PATH = os.getenv('/home/user/')