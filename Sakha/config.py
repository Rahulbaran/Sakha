import os
from dotenv import load_dotenv

load_dotenv(os.path.abspath('.env'))

basedir = os.path.abspath('Sakha')



class BaseConfig:

    """
    Base Configuration class containing default configuration and configuration
    applicable for all type of environments

    """

    # Default Configuration
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False


    # Configuration applicable for all type of environments
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 5*1024*1024
    RECAPTCHA_PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
    UPLOAD_PATH = basedir



# Configuration for development mode
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_DATABASE_URI') or 'sqlite:///Database/sakha.db'

# os.getenv('SQL_DATABASE_URI') or 

# Configuration for Testing mode
class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Database/test.db' 



# Configuration for production mode
class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', default='sqlite:///Database/prod.db')