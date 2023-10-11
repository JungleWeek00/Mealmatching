from flask import Blueprint, Flask, render_template, request, redirect, url_for, jsonify
import hashlib
from pymongo import MongoClient
authorize_bp = Blueprint('authorize', __name__)
# #https://scribblinganything.tistory.com/178

users = []

class User :
    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password
        self.selected_location = None

    def select_rest(self,location_name):
        self.selected_location = location_name

    def to_form(self):
        return {
            'name': self.name,
            'id' : self.id,
            'password': self.password,
        }
    

@authorize_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' :
        id_receive = id.form['id_give']
        password_receive = request.form['password_give']

        user = next((u for u in users if u.id == id_receive and u.password == password_receive), None)

        if user :
            response = redirect(url_for('locations.select_location'))
            response.set_cookie('id', id_receive)
            return response


    return render_template('login.html')

@authorize_bp.route('/register', methods = ['POST'])
# https://thalals.tistory.com/166
def register():
 
    name_receive = request.form['name_give']
    id_receive = id.form['id_give']
    password_receive = request.form['password_give']

    


    user = User(name_receive, id_receive, password_receive)
    users.append(user)




    return jsonify(message="User registered successfully"), 201

def get_login_user_info():
    id = request.cookies.get('id')
    user = next((u for u in users if u.id == id), None)
    return user







if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000, debug=True)



