'''This file will import all the things we need in this package so that it will be accessible to any module in the package'''

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

et = Flask(__name__,instance_relative_config=True) 
csrfobj = CSRFProtect(et)

from instance import config
et.config.from_pyfile("config.py")

db = SQLAlchemy(et)
migrate = Migrate(et,db)

from etapp.myroutes import admin,user
from . import myforms
from . import mymodels



       



@et.route('/admin/')
def admin():
    return render_template('dashboard.html')






if __name__=='__main__':
    et.run(debug=True,port=8085)