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

    SQLALCHEMY_TRACK_MODIFICATIONS = False   


class DevelopmentConfig(Config):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    """
    Testing application configuration
    """
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI =\
        'sqlite:////' + os.path.join(basedir, 'test_data.sqlite')

class ProductionConfig(Config):
    """
    Production application configuration
    """

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestingConfig
}