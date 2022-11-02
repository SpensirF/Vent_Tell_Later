from flask_app import app 
from flask import render_template, request, redirect, flash, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
from flask_app.models.appointment_model import Appointment
import re 

bcrypt = Bcrypt(app)



@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/user/registration', methods = ['POST'])
def register():
    if User.validate_registration(request.form) == False: 
        flash("This email already exists!", "error_registration_email")
        return redirect('/')
    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.create(data)
    session['name'] = data['name']
    session['email'] = data['email']
    session['user_id'] = user_id 
    return redirect('/dashboard') 

@app.route('/user/login', methods = ['POST'])
def process_login():
    current_user = User.get_one_to_validate_email(request.form)
    if current_user != None: 
        if not bcrypt.check_password_hash(current_user.password, request.form['password']): 
            flash("Wrong credentials", "error_login_creditials")
            return redirect('/')
        
        session['name'] = current_user.name
        session['email'] = current_user.email
        session['user_id'] = current_user.id
        return redirect('/dashboard')
    else:
        flash("Wrong credentials", "error_login_credentials")
        return redirect('/')



@app.route('/logout')
def logout_process():
    session.clear()
    return redirect('/')
