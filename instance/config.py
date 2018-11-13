import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    DATABASE_NAME = 'store_manager_3'
    # DATABASE_NAME = os.getenv('DATABASE_URL')
    

class DevelopmentConfig(Config):
    """Configuration fro Development."""
    DEBUG = True
    DATABASE_NAME = os.getenv('dbname')
    JWT_SECRET_KEY = os.getenv('SECRET')

class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_NAME = "test_store"
    JWT_SECRET_KEY = "heypeople"

class StagingConfig(Config):
    """Configuration for Staging."""
    DEBUG = False
    JWT_SECRET_KEY = "heypeople"

class ProductionConfig(Config):
    """Configration for Production"""
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = "heypeople"

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig
}