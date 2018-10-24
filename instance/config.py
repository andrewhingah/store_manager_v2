import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    DATABASE_NAME = 'store_manager_3'
    

class DevelopmentConfig(Config):
    """Configuration fro Development."""
    DEBUG = True
    DATABASE_NAME = 'store_manager_3'
    JWT_SECRET_KEY = "heypeople"

class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_NAME = "test_storemanager"
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