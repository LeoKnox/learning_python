import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "lyndakey"

    MONGODB_SETTINGS = { 'db' : 'pylyndachardb'}