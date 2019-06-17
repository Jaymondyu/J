#encoding: utf-8
from flask import Blueprint,render_template,url_for,request,make_response,Response,redirect,abort,json,session

blue=Blueprint('first_blue',__name__)


@blue.route('/')
def home():
    return render_template('index.html')

@blue.route('/mine')
def mine():

    hobbies = ['sInGInG','daNciNg','rAp','BasKeTBall']

    msg= '<h2>炮换机枪!炮换机枪!</h2>'

    return render_template('mine.html',hobbies=hobbies,msg=msg)
