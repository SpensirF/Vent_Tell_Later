from flask_app import app 
from flask import render_template, request, redirect, flash, session
from flask_app.models.appointment_model import Appointment


@app.route('/dashboard')
def display_appointment():
    if 'email' not in session: 
        return redirect('/')
    return render_template('dashboard.html')
    

@app.route('/confirmation')
def display_confirmation():
    if 'email' not in session: 
        return redirect('/')
    return render_template('confirmation.html')

@app.route('/appointment/made', methods = ['POST'])
def create_appointment(): 
    data = {
        **request.form,
        "user_id" : session['user_id']
    }
    appointment_id = Appointment.create(data)
    return redirect('/confirmation')