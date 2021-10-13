import datetime,mysql.connector
from etapp import db

class Stops(db.Model):
    __tablename__= 'bus_stops'
    stop_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    stop_name = db.Column(db.String(255),nullable=False)
    stop_route_id = db.Column(db.Integer(),db.ForeignKey('routes.route_id'),nullable=False)

    busroutes = db.relationship('Routes', backref='routing')

class Routes(db.Model):
    __tablename__= 'routes'
    route_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    route_name = db.Column(db.String(255),nullable=False)
    
    
    
    

class Buses(db.Model):
    __tablename__= 'buses'
    bus_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    bus_number = db.Column(db.Integer(),nullable=False)
    route_id = db.Column(db.Integer(),db.ForeignKey('routes.route_id'),nullable=False)

    busbus = db.relationship('Routes', backref='busing')

class Register(db.Model):
    __tablename__= 'user_registration'
    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_fname = db.Column(db.String(255),nullable=False)
    user_lname = db.Column(db.String(255),nullable=False)
    user_email = db.Column(db.String(255),nullable=False)
    user_password = db.Column(db.String(255),nullable=False)
    registered_on = db.Column(db.DateTime(),default=datetime.datetime.utcnow)
    # last_login_on = db.Column(db.DateTime(),default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow)

class Login(db.Model):    
    __tablename__= 'user_login'
    login_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(255),nullable=False)
    user_password = db.Column(db.String(255),nullable=False)
    login_on = db.Column(db.DateTime(),default=datetime.datetime.utcnow)

   

