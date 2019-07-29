from flask import Flask,render_template,request,redirect,url_for
import traceback

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('Login.html')

@app.route('/Login',methods=['POST'])
def login():
    username = request.form['user']
    password = request.form['password']

    if username == 'jaymondyu' and  password == 'plokijuh9':
        return render_template('database.html')
    else:
        return redirect(url_for('hello_world'))



if __name__ == '__main__':
    app.run(port=5000, debug=True)
