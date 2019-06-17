#encoding: utf-8
#会话技术:
    # 跨越请求传递数据
    # web开发中使用的短链接
    #
    # cookie
        # 客户端会话技术
        # 数据都是存储在浏览器中的
        # 支持过期
        # 不能跨域名
            # frame标签 (跨域时使用)
            # 可以直接加载整个网站
        # 不能跨浏览器
        # cookie是通过Response来进行操作的
        # Flask中的cookie可以直接支持中文
            # Flask对cookie中的内容进行了编码

    # session
        # 服务端会话技术
        # 对数据进行数据安全操作
        # 默认在内存内
        #     不容易管理
        #     容易丢失
        #     不能多台电脑协作
    # token



#用户登录
    # 1.用户中心
    # 2.用户登录
    # 3.用户推出


from flask import Flask,session
from App.views import blue
from flask_session import Session


app=Flask(__name__)

#设置secret key
app.config['SECRET_KEY'] = "plokijuh9"

#使用 flask-session 插件
# app.config['SESSION_TYPE']='.Redis'
# Session(app=app)

app.register_blueprint(blueprint=blue)


if __name__=='__main__':
    app.run(debug=True,port=3000)
