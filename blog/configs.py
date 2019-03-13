# _*_ coding:utf-8 _*_
# Author:Jazpenn

import logging
from logging.handlers import RotatingFileHandler


class Config:
    SECRET_KEY = 'MYKEY'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 6
    WTF_CSRF_SECRET_KEY = 'random key for form'  # for csrf protection

    @staticmethod
    def init_app(app):
        _handler = RotatingFileHandler(
                'log/flask-blog.log', maxBytes=10000, backupCount=1)
        _handler.setLevel(logging.WARNING)
        app.logger.addHandler(_handler)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://jazpenn:zxli201314@127.0.0.1/flask_blog'


class DefaultConfig(DevelopmentConfig):
    DEBUG = False


config = {
        'default':DevelopmentConfig
}
APP_CONFIG = DefaultConfig
