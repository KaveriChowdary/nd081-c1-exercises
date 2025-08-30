import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '5f3c1c3450988a787b42c00a18730b76'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'myserver156.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms (myserver156/cms)'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'odl_user_286385@udacityhol.onmicrosoft.com'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'dxkh08MFD*4s'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage15'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'a2BgfP9sFya+jhGDCONs4YooWZGoWMGzJwTI1iBNTgVa7dxY/nqOF8Tj0HqO/WLB07AWaj4NDFey+AStq+KSVw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    
