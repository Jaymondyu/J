#encoding: utf-8
from flask import Blueprint,render_template,url_for,request,make_response,Response,redirect,abort,json

blue=Blueprint('first_blue',__name__)

@blue.route('/')
def index():
    return "<h1>Hello world</h1>"

@blue.route('/urlfor/')
def url():
    r=url_for('second_blue.index')

# 导向 blue2 中的 index函数, 而不是blue中的index函数
    return r
