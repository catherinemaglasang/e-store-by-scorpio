import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    DEBUG = False
    TESTING = False
    DATABASE = 'postgresql://bookshop:bookshop@127.0.0.1:5432/bookshopdb'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DATABASE = 'postgresql://bookshop:bookshop@127.0.0.1:5432/test_bookshopdb'

class ProductionConfig(Config):
    DATABASE = 'mysql://user@localhost/foo'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
