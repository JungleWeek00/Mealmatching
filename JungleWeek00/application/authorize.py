from flask import Blueprint, Flask, render_template, request, redirect, url_for, jsonify
import hashlib
authorize_bp = Blueprint('auth', __name__)
# #https://scribblinganything.tistory.com/178

user = []

class User :
    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password
        self.selected_location = None

@authorize_bp.route('auth/login', methods = ['GET', 'POST'])
def login():
    

@authorize_bp.route('auth/register', methods = ['GET', 'POST'])
# https://thalals.tistory.com/166
def register():
    name_receive = request.form['name_give']
    id_receive = id.form['username_give']
    password_receive = request.form['password_give']

    password_hash = hashlib.she256(password_receive.encode('utf-8')).hexdigest()

    db.user.insert_one{'id': id_receive, 'pw' : password_hash , 'name' : name_receive}

    return jsonify({'result': 'success'})



