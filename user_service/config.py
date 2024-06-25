from os import environ

class Config:
	
  ##################### Application Configs #########################
	
	ENV = environ.get("VTS_USER_SERVICE_ENV", "production")
	DEBUG = bool(int(environ.get("VTS_USER_SERVICE_DEBUG", "0")))
	TESTING = bool(int(environ.get("VTS_USER_SERVICE_TESTING", "0")))
	SECRET_KEY = environ.get("VTS_USER_SERVICE_SECRET_KEY", "HARD-HARD-HARD-HARD-SECRET-KEY")
	
  ##################### Database Configs ############################
	
	SQLALCHEMY_DATABASE_URI = environ.get("VTS_USER_SERVICE_DATABASE_URI", None)
	SQLALCHEMY_ECHO = DEBUG
	SQLALCHEMY_RECORD_QUERIES = DEBUG
	SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
	