import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_RECORD_QUERIES = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	        'sqlite:///' + os.path.join(base_dir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(base_dir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(base_dir, 'data.sqlite')

	@classmethod
	def init_app(cls, app):
		Config.init_app(app)


class HerokuConfig(ProductionConfig):
	SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

	@classmethod
	def init_app(cls, app):
		ProductionConfig.init_app(app)

		# handle proxy server headers
		from werkzeug.contrib.fixers import ProxyFix
		app.wsgi_app = ProxyFix(app.wsgi_app)

		# log to stderr
		import logging
		from logging import StreamHandler
		file_handler = StreamHandler()
		file_handler.setLevel(logging.WARNING)
		app.logger.addHandler(file_handler)


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'heroku': HerokuConfig,
	'default': DevelopmentConfig
}