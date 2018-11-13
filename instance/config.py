import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    DATABASE_NAME=os.getenv("DB_NAME")
    JWT_SECRET_KEY=os.getenv("SECRET")
    

class DevelopmentConfig(Config):
    """Configuration fro Development."""
    DEBUG = True
    JWT_SECRET_KEY=os.getenv("SECRET")

class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_NAME="test_store"
    JWT_SECRET_KEY="secretsecret"

class StagingConfig(Config):
    """Configuration for Staging."""
    DEBUG = False
    JWT_SECRET_KEY = "heypeople"

class ProductionConfig(Config):
    """Configration for Production"""
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY=os.getenv("SECRET")


app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig
}