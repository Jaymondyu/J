import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/Tool/')
def Tool():
    return flask.render_template('Tool.html')

@app.route('/CPGS/')
def CPGS():
    return flask.render_template('CPGS.html')

@app.route('/Genes/')
def Genes():
    return flask.render_template('Genes.html')

@app.route('/Correlation/')
def Correlation():
    return flask.render_template('Correlation.html')

@app.route('/Survival/')
def Survival():
    return flask.render_template('survival.html')

@app.route('/Genes_DIY/')
def Genes_DIY():
    return flask.render_template('Genes_DIY.html')

@app.route('/Correlation_DIY/')
def Correlation_DIY():
    return flask.render_template('Correlation_DIY.html')

@app.route('/Survival_DIY/')
def Survival_DIY():
    return flask.render_template('Survival_DIY.html')

@app.route('/About/')
def About():
    return flask.render_template('About.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
