
# -*- coding: UTF-8 -*-
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request,session,escape
#from flask.ext.login import LoginManager,
from flask_mysqldb import MySQL
from hashlib import md5
from passlib.hash import sha256_crypt
import MySQLdb
import csv
from functools import wraps
from flask_user import roles_required
import hashlib
import hmac
from flask_sqlalchemy import SQLAlchemy
import numpy
import sys
from passlib.hash import sha256_crypt
app = Flask(__name__)
app.secret_key = '123'
db = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="escpj")
cur = db.cursor()
db.set_character_set('utf8')
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form.get("username",False)
        password_input = request.form.get("password",False)
        #cur = db.cursor()
        data=cur.execute(("SELECT passwd  FROM usertable WHERE username='{}'").format(username))
        if data>0:
            password=cur.fetchone()[0]
            if (password==password_input):
                session['logged_in'] = True
                session['username'] = username
                rol=cur.execute(("SELECT role  FROM usertable WHERE username='{}'").format(username))
                role=cur.fetchone()[0]
                if role=='admin':
                    session['role'] = 'admin'
                    flash('You are now logged in', 'success')
                    return redirect('/home')
                else:
                    session['role'] = 'user'
                    flash('You are now logged in', 'success')
                    return redirect('/home')
            else:
                error = 'password not match'
                #error = password_input
                return render_template('login.html', error=error)

        else:
            error='user not exist'
            return render_template('login.html',error=error)
    return render_template('login.html')




def is_log_in(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('Please log in','danger')
            return redirect('/')
    return wrap


def permission_required(f):

    @wraps(f)
    def decorate_func(*args,**kwargs):
        if session['role']=='admin':
            return f(*args,**kwargs)
        else:
            return redirect('/home')
    return decorate_func


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now log out','success')
    return redirect(url_for('login'))



@app.route('/home',methods=['GET','POST'])
@is_log_in
def home():
	return render_template('homeadmin.html')




@app.route('/role',methods=['GET','POST'])
@is_log_in
@permission_required
def manage():
	cur.execute("SELECT * FROM `users`;")
	rows=cur.fetchall()
	return render_template('manage.html',rows=rows)






if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80,debug=True)
