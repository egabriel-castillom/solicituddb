from flask import Flask, jsonify, render_template,session,request
from dotenv import load_dotenv
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
        return render_template('index.html')

    @app.route('/get-data',methods=('POST','GET'))
    def get_data():
        return jsonify(x='Hola Mundo')
    return app

app = crear_app()
