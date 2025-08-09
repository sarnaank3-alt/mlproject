# Configuration settings for the backend services

import os

class Config:
    # General settings
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')

    # AWS settings
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    RDS_ENDPOINT = os.getenv('RDS_ENDPOINT')
    RDS_DB_NAME = os.getenv('RDS_DB_NAME')
    RDS_USERNAME = os.getenv('RDS_USERNAME')
    RDS_PASSWORD = os.getenv('RDS_PASSWORD')

    # OpenAI settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')
    OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', 0.0))
    OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', 1024))

    # Tool call limits
    TOOL_CALL_LIMIT = int(os.getenv('TOOL_CALL_LIMIT', 25))

    # Database settings
    DB_CONNECTION_STRING = f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_ENDPOINT}/{RDS_DB_NAME}"

    # Logging settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')