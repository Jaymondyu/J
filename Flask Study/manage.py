# encoding=utf-8
from flask import Flask,render_template,url_for,request,make_response,Response,redirect,abort,json
import uuid
# import json

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"
@app.route('/hello/')
def hello():
    return render_template("hello.html")

#关键字参数
# 默认标识是尖括号<name>
# name需要和对应的视图函数的参数名字保持一致
# 参数允许有默认值. 如果有,那么在路由中,不传输参数也是ok的. 如果没有,参数路由中必须传递
# 默认参数类型是字符串
# 参数语法 <converter:var>
# converter类型
# string 默认类型,会将斜线认为是参数分割
# int
# float
# path 接收到的数据格式是字符串,但会将斜线认为是一个字符
# uuid 限制参数为uuid格式
# any 只能在给出的元祖中选择（和枚举一个意思）
@app.route('/params/<hehe>/')
def params(hehe):
    print(type(hehe))
    print(hehe)
    return "获取参数"

@app.route('/get/<path:name>/')
def get(name):
    print(type(name))
    print(name)
    return "获取参数name"

@app.route('/getuuid/')
def get_uuid():
    return str(uuid.uuid4())

@app.route('/any/<any(c,d,e):an>/')
def any(an):
    print(an)
    print(type(an))
    return "ANY"


#请求方式
# 请求方法要自己配置
# 在地址后加上method, 列表格式,内跟地址的请求方式
# 如: methods['GET','POST','DELETE','HEAD','PUT']
@app.route('/getpostuuid/',methods=['GET','POST'])
def getpost_uuid():
    return str(uuid.uuid4())

#反向解析
# url_for
#根据 函数名(endpoint) 获取到对应的路径
#在模板中可以直接使用
@app.route('/url/')
def url():
    print(url_for('get_uuid'))
#参数可以以value的形式加上
    print(url_for('any',an='c'))
    return "反向解析"


#Request 内置对象
@app.route('/request/',methods=["GET","POST"])
def req():
    # print(request)
    # print(type(request))
    #
    # print(request.method)
    # print(request.data)
    # # arguments 参数  get请求参数
    print(request.args.get('name'))
    print(request.args.getlist('password'))
    # #post 相关请求都会有数据
    # print(request.form)
    # print(request.files)
    # print(request.cookies)
    # # print(request.json)
    # print(request.remote_addr)
    # #浏览器身份
    # print(request.user_agent)
    # print(request.url)


    return "请求"


#Response
#视图函数返回接受两种类型
# Response对象
# 字符串
# 针对字符串会帮我们包装成Response

@app.route('/response/')
def resp():
    #直接response, 返回字符串
    # result= render_template('hello.html')
    # print(result)
    # print(type(result))
    # return "<h2>响应</h2>"

    # 使用make_response, 制作一个响应进行返回
    # response=make_response('<h2>DIET Coke Response</h2>')
    # print(response)
    # print(type(response))
    # return response

    #自写response,直接创建response进行返回
    response=Response(response='<h2>response</h2>',status='200')
    print(response)
    print(type(response))
    return response

    #返回的都是 response对象

#重定向
@app.route('/redirect/')
def redir():

    # 直接redirect
    return redirect(url_for('hello'))


    #使用response实现redirect
    # response=redirect(url_for('hello'))
    # print(response)
    # print(type(response))
    # return response


 # 终止执行
 # 无论什么方式请求 会返回我们想返回的错误
@app.route("/abort/")
def ab():

    abort(405)


#返回json
@app.route('/json/')
def json_transf():

    #将数据格式化成json格式先,在同时设置返回类型为application/json
    # result=json.jsonify({'name':'value'})
    # result=json.jsonify(name='value',age=18)

    #json.dumps将数据格式化成json格式先,没有设置返回的类型,默认的类型是text/html
    result_1=json.dumps({'name':'value','age':'18'})

    # print(result)
    # print(type(result))
    print(result_1)
    print(type(result_1))

    return result_1













if __name__=='__main__':
    app.run(debug=True,port=3000)
