from flask import Flask
from App.views import blue
from App.views2 import blue as blue2


app=Flask(__name__)

app.register_blueprint(blueprint=blue)
app.register_blueprint(blueprint=blue2)


if __name__=='__main__':
    app.run(debug=True,port=3000)
