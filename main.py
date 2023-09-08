from flask import Flask, jsonify, render_template,session,request
from dotenv import load_dotenv
from db import get_connection,execute_query
from sendEmail import send_email
import click
import os
import time

load_dotenv()

def roundId():
    id = request.form.get('id')
    session['id'] = id                                
    message = '(' + id + ') id en sesión 1.'
    if session.get('P') == None:      
        session['P'] = '0'
    return jsonify(id=id)        

def roundID():
    id = session.get('id')
    iD = request.form.get('id')
    session['iD'] = iD                    
    message = '(' + id + ') , (' + iD + ') ids en sesion.'             
    a = float(id)
    b = float(iD)
    RF = a + b
    rf = str(RF)
    results=[1.1, 2.2, 3.3, 4.4, 5.55, 6.66]
    if id == iD:
        same = 1
        session.pop('iD')
        message=str(id) +' ya se ha seleccionado en la ronda actual.'
        return jsonify(id = id,same=same)
    elif RF in results:
        rfo = 'CORRECTO'
        p = session.get('P')
        P = str(int(p)+1)
        session['P'] = P
        PA = 'PUNTAJE ACTUAL: ' + P
        appendSessionList(id)
        appendSessionList(iD)
        session.pop('id',None)
        session.pop('iD',None)
        return jsonify(id=iD,rf=rfo,PA=PA)
    else:
        rfo = 'INCORRECTO'
        session.pop('id',None)
        session.pop('iD',None)
        session['F'] = 1
        F = session.get('F')
        return jsonify(id=iD,rf = rfo,F=F)

def appendSessionList(item):
    l = session['l']
    l.append(item)
    session['l']=l
    return session['l']

def getStrList():
    l = session['l']
    strList = str(l)
    return strList

def crear_app():
    app = Flask(__name__)
    app.config.from_mapping( 
        SECRET_KEY=os.environ.get('SECRET_KEY'),        
    )

    @app.route('/',methods=('POST','GET'))
    def index():
        return render_template('index.html')

    @app.route('/mem0',methods=('POST','GET'))
    def mem0():
        session.clear()
        session['l'] = []
        my_rounds=['1','2','3','4','5','6']
        my_l=[0,1,2,3,4,5,6,7,8,9,10,11]
        my_dict = {}
        for round_, pair in zip(my_rounds, zip(my_l[::2], my_l[1::2])):
            my_dict[round_] = pair
        session['my_dict'] = my_dict
        return render_template('indexmem0.html')

    @app.route('/get-data',methods=('POST','GET'))
    def get_data():
        if request.method=='POST':
            if session.get('P') == '5':
                if session.get('id'):
                    return roundID()
                else:
                    return roundId()
            if session.get('P') == '4':
                if session.get('id'):
                    return roundID()
                else:
                    return roundId()
            if session.get('P') == '3':
                if session.get('id'):
                    return roundID()
                else:
                    return roundId()
            if session.get('P') == '2':
                if session.get('id'):
                    return roundID()
                else:
                    return roundId()
            if session.get('P'):
                if session.get('id'):
                    return roundID()
                else:
                    return roundId()
            elif session.get('id'):
                return roundID()
            elif request.form.get('id') == 'x':
                id = 1
                session['start'] = id
                return jsonify(message='')
            elif session.get('start'):
                return roundId()
        elif request.method=='GET':
            if session.get('F'):
                session.pop('F',None)
                return jsonify(message='',rfo='')
            else:
                P = 0            
                session.clear()
                return jsonify(x='')

    @app.route('/db', methods=['POST'])
    def db():
        name = request.form['data1']
        email = request.form['data2']
        message = request.form['data3']
        query = 'INSERT INTO users (uname,uemail,umessage) VALUES (%s,%s,%s)'
        params = (name,email,message)
        results = execute_query(get_connection(),query,params)        

        subject = "Email test from Portfolio"
        sender = "senderfromportfolio@gmail.com"
        receiver = "receiverfromportfolio@gmail.com"
        body = 'New message from ' + name + ' (' + email + ') :' + message
        password = "zphmjzagipcdjusy"

        send_email(subject, sender, receiver, body, password)
        
        return 'n'

    return app

app = crear_app()
