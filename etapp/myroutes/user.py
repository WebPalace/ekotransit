from flask import render_template,make_response,abort,request,redirect,flash,session
from werkzeug.security import generate_password_hash,check_password_hash
from etapp import et,db
from etapp.mymodels import Register,Login,Stops,Routes
from etapp.myforms import Registration, UserLogin

@et.route('/',methods=['GET','POST'])
def home():
    loggedin = session.get('userid')
    data = Register.query.filter(Register.user_id == loggedin).first()
    deets = Stops.query.all()
    a = request.form.get('location')
    b = request.form.get('destination')
    if request.method == 'GET' and loggedin != None:
        return render_template('user/ethome.html',data=data,a=a,b=b,deets=deets)
    else:
        return redirect('/login/')
    

@et.route('/navigate/',methods=['GET','POST'])
def navigation():
    loggedin = session.get('userid')
    data = Register.query.filter(Register.user_id == loggedin).first()
    a = request.form.get('location')
    b = request.form.get('destination')
    deets = Stops.query.filter(Stops.stop_name==a).first()
    deets2 = Stops.query.filter(Stops.stop_name==b).first()
    return render_template('user/etnavpage.html',a=a,b=b,deets=deets,deets2=deets2,data=data)

@et.route('/breakdown/',methods=['GET','POST'])
def journey():
    loggedin = session.get('userid')
    selection1 = request.form.get('routesel1')
    selection2 = request.form.get('routesel2')
    routedis1 = request.form.get('routedis1')
    routedis2 = request.form.get('routedis2')
    data = Register.query.filter(Register.user_id == loggedin).first()
    deets = Routes.query.filter(Routes.route_name==routedis1).first()
    deets2 = Routes.query.filter(Routes.route_name==routedis2).first()
    return render_template('user/etbreakdown.html',deets=deets,deets2=deets2,data=data,selection1=selection1,selection2=selection2,routedis1=routedis1,routedis2=routedis2)

@et.route('/login/',methods=['GET','POST'])
def loginpage():
    if request.method == 'GET':
        return render_template('user/etlogin.html')

@et.route('/about/')
def about():
    return render_template('user/etabout.html')

@et.route('/mylogin/',methods=['POST','GET'])
def userlogin():
    form = UserLogin()
    if request.method == 'GET':
        return render_template('user/etmylogin.html',form=form)
    else:
        if form.validate_on_submit():
            user = form.email.data
            pwd = form.password.data
            search = db.session.query(Register).filter(Register.user_email == f'{user}').first()
            if search != None : 
                stored_hash = search.user_password
                check = check_password_hash(stored_hash,pwd)
                if check:
                    session['userid'] = search.user_id
                    flash('Login Succesful!')
                    return redirect ('/')
                else:
                    flash('Invalid Credentials')
                    return redirect('/mylogin/')
            else:
                flash('Invalid Credentials')
                return redirect('/mylogin/')
        else:
            return render_template('user/etmylogin.html',form=form)

@et.route('/register/',methods=['GET','POST'])
def registration():
    form = Registration()
    if request.method == 'GET':
        return render_template('user/etregister.html',form=form)
    else:
        fname = form.userfname.data
        lname = form.userlname.data
        email = form.email.data
        pwd = form.password.data
        enc_pwd = generate_password_hash(pwd)
        r = Register(user_fname=f'{fname}',user_lname=f'{lname}',user_email=f'{email}',user_password=f'{enc_pwd}')
        db.session.add(r)
        db.session.commit()
        session['userid']= r.user_id 
        msg = flash('Registration Succesful')
        return redirect('/')

@et.errorhandler(404)  
def pagenotfound(error):
    return (render_template('user/error.html',error=error),404) 

@et.route('/logout/')
def logout():
    if session.get('userid') != None:
        session.pop('userid')
    return redirect('/mylogin/')