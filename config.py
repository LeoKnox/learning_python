import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "lyndakey"

    MONGODB_SETTINGS = { 'db' : 'pylyndachardb'}