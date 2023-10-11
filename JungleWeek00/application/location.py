from flask import Blueprint, Flask, render_template, request, redirect, url_for, jsonify
from application import location
from pymongo import MongoClient

location_bp = Blueprint('location', __name__)
# #https://scribblinganything.tistory.com/178

class Location :
    def __init__(self, number, location_name, count = 0):
        self.number = number
        self.location_name = location_name
        self.count = count
    
locations = [{"number" : "1" , "name" : "경기드림타워", "count" : 0},
            {"number" : "2" , "name" : "경기드림타워", "count" : 0},
            {"number" : "3" , "name" : "경기드림타워", "count" : 0},
            {"number" : "4" , "name" : "경기드림타워", "count" : 0},
            {"number" : "5" , "name" : "경기드림타워", "count" : 0}]
# 식당선택
@location_bp.route('/select_location', methods = ['GET', 'POST'])

def select_rest() :
    if not check_user_login():
        return redirect(url_for('authorize.login'))
    
    if request.method == 'POST' :
        location_name = request.form['location']
        user = get_login_user_info()
        user.selected_location = location_name
        update_select_count(location_name)

    return render_template('location_select.html', locations = locations)

#식딩 정보
@location_bp.route('/location/<location_name>')
def location_info(location_name):
    location = next((loc for loc in locations if loc['name'] == location_name), None)
    return render_template('location_info.html', location=location)
# 로그인확인
def check_user_login() :
    return 'username' in request.cookies

def get_login_user_info() :
    
    id = request.cookies.get('id')
    user = next((u for u in users if u.id == id), None)
    return user
    
# 식당 선택 후 n 수 
def update_select_count(location_name):
    location = next((rest for rest in locations if rest['name'] == location_name), None)
    # next함수 : https://dojang.io/mod/page/view.php?id=2408
    if  location:
        location['count'] +=1
