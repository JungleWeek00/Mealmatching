from flask import Blueprint, Flask, render_template, request, redirect, url_for, jsonify

location_bp = Blueprint('location', __name__)
# #https://scribblinganything.tistory.com/178

class Location :
    def __init__(self, number, location_name, count = 0):
        self.number = number
        self.location_name = location_name
        self.count = count
    
locations = [{"number" : "1" , "location_name" : "경기드림타워", "count" : 0},
            {"number" : "2" , "location_name" : "경기드림타워", "count" : 0},
            {"number" : "3" , "location_name" : "경기드림타워", "count" : 0},
            {"number" : "4" , "location_name" : "경기드림타워", "count" : 0},
            {"number" : "5" , "location_name" : "경기드림타워", "count" : 0}]
# 식당선택
@location_bp.route('/location', methods = ['GET', 'POST'])

def select() :
    if user_login is not  :

        




#식딩 정보
@location_bp.route('/location', methods = ['GET', 'POST'])
# 로그인확인
def user_login() :
    return 'username' in request.cookies

def login_user_info() :
    'username' 
# 식당 선택 후 n 수 
def update_select_count(location_name):
    location = next(rest in rest for location['name'] in location)
    # next함수 : https://dojang.io/mod/page/view.php?id=2408
    if  :
        count+1


