from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask_jwt_extended
from application.authorize import authorize_bp
from application.location import location_bp

from pymongo import MongoClient 
from bson.json_util import dumps

app = Flask(__name__)
app.register_blueprint(authorize_bp)
app.register_blueprint(location_bp)
#https://scribblinganything.tistory.com/178
client = MongoClient('mongodb://localhost:~')
db = client['db']


if __name__ == '__main__':  
   app.run(debug=True)