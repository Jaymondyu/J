from flask import Flask,render_template,request,redirect,url_for
import traceback
import mysql.connector
import json

app = Flask(__name__)


conn = mysql.connector.connect(user = 'root',password ='plokijuh9',database ='account') #连接数据库，创建Flask_app数据库
cursor = conn.cursor()


@app.route('/')
def hello_world():
    return render_template('Login.html')

@app.route('/Login/',methods=['POST'])
def login():
    username = request.form['user']
    pwd = request.form['password']

    if username == 'jaymondyu' and  pwd == 'plokijuh9':
        return render_template('database.html')
    else:
        return redirect(url_for('hello_world'))

@app.route('/list/',methods=['POST'])
def list():

    # 编写查询语言
    sql= "select * FROM account"
    # 执行查询语言
    cursor.execute(sql)
    # 获取结果
    result = cursor.fetchall()
    # 执行条数查询
    return result


if __name__ == '__main__':
    app.run(port=5000, debug=True)
