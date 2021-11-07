from logging import DEBUG
import os

class Config:
  '''
  Class with general configuratiobs for the app
  '''
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:mwendaB@localhost/pitcher'
  
  SECRET_KEY= 'mwendaB'
  UPLOADED_PHOTOS_DEST='app/static/photos'

  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
  
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  '''

  DEBUG=True 
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:mwendaB@localhost/pitcher'


class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:mwendaB@localhost/pitcher'
  DEBUG = True
config_options={
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}


 
  