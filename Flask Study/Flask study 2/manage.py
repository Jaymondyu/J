from flask import Flask,render_template,url_for,request,make_response,Response,redirect,abort,json
from App.views import blue


app=Flask(__name__)

app.register_blueprint(blueprint=blue)


if __name__=='__main__':
    app.run(debug=True,port=3000)
