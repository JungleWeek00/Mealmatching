from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, g, flash
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
# import logging
import datetime
from bson import ObjectId

g_username = ''

app = Flask(__name__)

#https://scribblinganything.tistory.com/178

uri = "mongodb+srv://daeun:daeun0101@cluster0.sdxyqrk.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.team1week00

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# MongoDB 컬렉션 설정
users= db.users
locations= db.locations

# -------------몽고디비 연결되었나 확인-----------
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# ---------------------------------------------------

app.secret_key = "MY"
# 장소 추가 

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user input from the form
        username = request.form.get('username')
        password = request.form.get('password')
        number = request.form.get('number')
        select_location = None

        user_data = {'username': username, 'password': password, 'number': number, 'select_location':select_location}
        # 3. mongoDB에 데이터 넣기

        if users.find_one({'username': username}):
            # error
            flash("중복된 아이디 입니다")
            return render_template('register.html')
        else:
            users.insert_one(user_data)

        # Render a template using Jinja2 to display a response
        return render_template('login.html')

    # Render the registration form
    return render_template('map.html')


@app.route('/register', methods=['POST'])
def move():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        if users.find_one({'username': username}):
            user = users.find_one({'username': username})
            if user['password'] == password:
                print('wowowowowowow')
                global g_username 
                g_username = user['username']
                

                print(g_username)
                return render_template('newmap.html', user=user)
            else:
                flash("아이디 혹은 비밀번호를 확인하세요")
                return render_template('login.html')
        else:
            # username이 db에 없을시 error
            flash("아이디 혹은 비밀번호를 확인하세요")
            return render_template('login.html')
    else:
        return render_template('login.html')
    

@app.route('/info/<string:locations_id>', methods=['GET', 'POST'])
def info(locations_id):
    print('123')
    if request.method == 'GET':
        location_info = locations.find_one({'number': locations_id})
        # 모든 유저 돌면서, users 테이블의 selected_location이 locations_id일경우 1씩 더해서 총 명수 구해

        cnt = users.count_documents({'select_location':location_info['number']})
        #cnt = users.count({select_location : location_info['number']})

        
        if location_info:
        # info.html로 위치 정보 전달
            return render_template('info.html', dic1=location_info, location_cnt=cnt)
        else:
        # 정보를 찾지 못한 경우에 대한 처리
            return "Location not found"
        
@app.route('/join/<string:locations_id>', methods=['GET'])
def join(locations_id):
    # MongoDB에서 해당 위치 정보 가져오기
    location_info = locations.find_one({'number': locations_id})
    
    global g_username
    if location_info:
        # "people" 수를 1 증가시키고  업데이트

        if (users.find_one({'username': g_username})['select_location']):
            base_select_location = users.find_one({'username': g_username})['select_location']
        else :
            base_select_location = None

        if base_select_location == None:
            flash("참여되었습니다.")
            users.update_one({'username': g_username}, {'$set': {'select_location': locations_id}})
        elif base_select_location == location_info['number'] :
            flash("이미 선택된 음식점입니다.")
        elif base_select_location != location_info['number'] :
            flash("음식점을 변경하셨습니다.")
            users.update_one({'username': g_username}, {'$set': {'select_location': locations_id}})
        else : 
            flash("참여되었습니다.")
            users.update_one({'username': g_username}, {'$set': {'select_location': locations_id}})


    # info.html로 리디렉션
    return redirect('/info/{}'.format(locations_id))



if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/display_users')
# def display_users():
#     users_info = users.find({}, {'_id': 0})
#     users_list = [user for user in users_info]
#     return jsonify(users_list)

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)