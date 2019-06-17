#encoding: utf-8
from flask import Blueprint,render_template,url_for,request,make_response,Response,redirect,abort,json,session

blue=Blueprint('first_blue',__name__)


@blue.route('/')
def home():

    #取出存储的用户名cookie
    # username = request.cookies.get('user')

    #取出存储的用户名session
    username = session.get('user')

    return render_template('Home.html', username = username)


@blue.route('/login/',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('Login.html')
    elif request.method == "POST":

        username = request.form.get('username')

        # print(username)

        resp = Response(response='登陆成功 %s' % username)

        #将 输入的 用户名 存入cookie中
        # resp.set_cookie('user',username)

        #将 输入的 用户名 存入session中
        session['user']= username

        #使用session时 需要在manage中写secret key

        return resp

@blue.route('/logout/')
def logout():

    resp= redirect(url_for('first_blue.home'))

    # 删除cookie
    resp.delete_cookie('user')

    return resp


# 多个路由同时加载同一个模板
@blue.route('/hello/')
@blue.route('/hi/')
def hello():
    return render_template('hello.html')
