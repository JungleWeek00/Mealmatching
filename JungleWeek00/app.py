from flask import Flask, render_template, request, redirect, url_for, jsonify
from application.authorize import authorize_bp
from application.location import location_bp

from pymongo import MongoClient 
from bson.json_util import dumps

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.register_blueprint(authorize_bp)
app.register_blueprint(location_bp)
#https://scribblinganything.tistory.com/178
client = MongoClient('localhost', 27017)
db = client.team1db

# MongoDB 컬렉션 설정
users_collection = db['users']
locations_collection = db['locations']

def save_user(user):
    users_collection.insert_one({
        'name': user.name,
        'username': user.username,
        'password': user.password,
        'selected_location': user.selected_location
    })

def save_location(location):
    locations_collection.insert_one({
        'number': location.number,
        'location_name': location.name,
        'count': location.count
    })

# log 확인 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id_receive = request.form['id_give']
        password_receive = request.form['password_give']

        user = next((u for u in users if u.id == id_receive and u.password == password_receive), None)

        if user:
            app.logger.info(f'User {user.id} logged in')
            response = redirect(url_for('location.select_location'))
            response.set_cookie('id', id_receive)
            return response

    return render_template('login.html')






if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000, debug=True)