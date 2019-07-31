import flask
import traceback
import mysql.connector
import json

app = flask.Flask(__name__)


conn = mysql.connector.connect(user = 'root',password ='plokijuh9',database ='人员账号管理') #连接数据库，创建Flask_app数据库
cursor = conn.cursor()


@app.route('/')
def hello_world():
    return flask.render_template('Login.html')

@app.route('/Login',methods=['POST'])
def login():
    username = flask.request.form['user']
    pwd = flask.request.form['password']

    if username == 'jaymondyu' and  pwd == 'plokijuh9':
        return flask.redirect(flask.url_for('index'))
    else:
        return flask.redirect(flask.url_for('hello_world'))

@app.route('/index/',methods=['GET'])
def index():
    return flask.render_template('database.html')



@app.route('/list/',methods=['POST'])
def list():

    # 编写查询语言
    search = flask.request.values['MMP']
    sql= str(search)
    # 执行查询语言
    cursor.execute(sql)
    # 获取结果
    result = cursor.fetchall()
    # 执行条数查询

    # print (json.dumps(result))
    return json.dumps(result)

@app.route('/add/',methods=['POST'])
def add():

    a1 = "Success"

    name = flask.request.values['name']
    account = flask.request.values['account']

    print (name)
    print (account)
    return json.dumps(a1)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
