#encoding:utf-8
# 可以在不同的 view中 写路由, 最后都能导入
# 只要地址不冲突就行
# 函数名是可以一样的

from flask import Blueprint,render_template,url_for,request,make_response,Response,redirect,abort,json

blue=Blueprint('second_blue', __name__)


@blue.route('/index/')
def index():
    return "<h1>This is the true index</h1>"
