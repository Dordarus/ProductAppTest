import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =\
        'sqlite:////' + os.path.join(basedir, 'data.sqlite')

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopmentConfig(Config):
    """
    Development application configuration
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI =\
        'sqlite:////' + os.path.join(basedir, 'test_data.sqlite')

class ProductionConfig(Config):
    """
    Production application configuration
    """
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestingConfig
}