import os


class Config(object):
    SECRET_KEY = 'random string'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vouchers.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
