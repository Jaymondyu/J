from flask import Flask,render_template
import uuid

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

if __name__=='__main__':
    app.run(debug=True,port=3000)
