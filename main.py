from flask import Flask, jsonify, render_template,session,request
from dotenv import load_dotenv
from db import get_connection,execute_query
from sendEmail import send_email
import click
import os
import time

load_dotenv()

def crear_app():
    app = Flask(__name__)
    app.config.from_mapping( 
        SECRET_KEY=os.environ.get('SECRET_KEY'),        
    )

    @app.route('/',methods=('POST','GET'))
    def index():
        return render_template('form.html')

    @app.route('/getdata', methods=['GET'])
    def getdata():
        query = 'SELECT * FROM users'
        results = execute_query(get_connection(), query)
        return jsonify(results)

    @app.route('/db', methods=['POST'])
    def db():
        folio = request.form['folio']
        client = request.form['client']
        d = request.form['d']
        flet = request.form['flet'] == 'true'
        isr = request.form['isr'] == 'true'
        p1prod = request.form['p1prod']
        p1mad = request.form['p1mad']
        p1med = request.form['p1med']
        p1u = request.form['p1u']
        p1c = request.form['p1c']
        p1t = request.form['p1t']
        p2prod = request.form['p2prod']
        p2mad = request.form['p2mad']
        p2med = request.form['p2med']
        p2u = request.form['p2u']
        p2c = request.form['p2c']
        p2t = request.form['p2t']
        p3prod = request.form['p3prod']
        p3mad = request.form['p3mad']
        p3med = request.form['p3med']
        p3u = request.form['p3u']
        p3c = request.form['p3c']
        p3t = request.form['p3t']
        p4prod = request.form['p4prod']
        p4mad = request.form['p4mad']
        p4med = request.form['p4med']
        p4u = request.form['p4u']
        p4c = request.form['p4c']
        p4t = request.form['p4t']
        p5prod = request.form['p5prod']
        p5mad = request.form['p5mad']
        p5med = request.form['p5med']
        p5u = request.form['p5u']
        p5c = request.form['p5c']
        p5t = request.form['p5t']
        p6prod = request.form['p6prod']
        p6mad = request.form['p6mad']
        p6med = request.form['p6med']
        p6u = request.form['p6u']
        p6c = request.form['p6c']
        p6t = request.form['p6t']
        unotas = request.form['unotas']
        query = 'INSERT INTO users (folio, client, d, flet, isr, p1prod, p1mad, p1med, p1u, p1c, p1t, p2prod, p2mad, p2med, p2u, p2c, p2t, p3prod, p3mad, p3med, p3u, p3c, p3t, p4prod, p4mad, p4med, p4u, p4c, p4t, p5prod, p5mad, p5med, p5u, p5c, p5t, p6prod, p6mad, p6med, p6u, p6c, p6t, unotas) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)'
        params = (folio, client, d, flet, isr, p1prod, p1mad, p1med, p1u, p1c, p1t, p2prod, p2mad, p2med, p2u, p2c, p2t, p3prod, p3mad, p3med, p3u, p3c, p3t, p4prod, p4mad, p4med, p4u, p4c, p4t, p5prod, p5mad, p5med, p5u, p5c, p5t, p6prod, p6mad, p6med, p6u, p6c, p6t, unotas)
        results = execute_query(get_connection(), query, params)
            
        return 'n'

    return app

app = crear_app()
