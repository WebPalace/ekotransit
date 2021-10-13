from os import environ,path
from dotenv import load_dotenv

basedir=path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))
SECRET_KEY=environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI= 'mysql+mysqlconnector://root@localhost/ekotransit'
SQLALCHEMY_TRACK_MODIFICATIONS=True


FLASK_DEBUG="True"
FLASK_ENVIRONMENT='development'
ADMIN_EMAIL='admin@pytapp.com'

