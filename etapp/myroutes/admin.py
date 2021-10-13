from flask import render_template,make_response,abort,request,redirect,flash,session
from werkzeug.security import generate_password_hash,check_password_hash
from etapp import et,db
from etapp.mymodels import Register,Login,Buses,Routes,Stops
from etapp.myforms import Registration, UserLogin,AdminLogin

@et.route('/admin/',methods=['POST','GET'])
def adminpage():    
    loggedin = session.get('userid')
    routes = Routes.query.all()
    b = Stops.query.filter(Stops.stop_route_id == '1').all()
    b2 = Stops.query.filter(Stops.stop_route_id == '2').all()
    b3 = Stops.query.filter(Stops.stop_route_id == '4').all()
    if request.method == 'GET' and loggedin != None:
        return render_template('admin/dashboard.html',b=b,b2=b2,routes=routes,b3=b3)
    else:
        return redirect('/adminlogin/')

@et.route('/newroute/',methods=['POST','GET'])
def addroute():
    rname = request.form.get('route2')
    r = Routes(route_name=rname)
    db.session.add(r)
    db.session.commit()
    msg = flash('Route Added Succesfully')
    return redirect('/admin/')

@et.route('/newstop/',methods=['POST','GET'])
def addstop():
    sname = request.form.get('stop')
    sroute = request.form.get('myroute')
    s = Stops(stop_name=sname,stop_route_id=sroute)
    db.session.add(s)
    db.session.commit()
    msg = flash('Stop Added Succesfully')
    return render_template('admin/dashboard.html',msg=msg)

@et.route('/deletestop/',methods=['POST','GET'])
def deletestop():
    mystops = request.form.getlist('stopid1[]')
    for i in mystops:
        delstops= Stops.query.filter(Stops.stop_id == i).all()
        db.session.delete(delstops)
        db.session.commit()
    msg = flash('Stop(s) Deleted Succesfully')
    return render_template('admin/dashboard.html',msg=msg)

@et.route('/adminlogin/',methods=['POST','GET'])
def adminlogin():
    form = AdminLogin()
    if request.method == 'GET':
        return render_template('admin/etadminlogin.html',form=form)
    else:
        if form.validate_on_submit():
            user = 'admin@etapp.com'
            pwd = '1234'
            if user and pwd: 
                session['adminid'] = user
                flash('Login Succesful!')
                return redirect ('/admin/')
            else:
                flash('Invalid Credentials')
                return redirect('/adminlogin/')
        else:
            flash('Invalid Credentials')
            return redirect('/adminlogin/')

@et.route('/adminlogout/')
def adminlogout():
    if session.get('adminid') != None:
        session.pop('adminid')
    return redirect('/adminlogin/')
        