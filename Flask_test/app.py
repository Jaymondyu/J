# -*- coding: utf-8 -*-

import flask
import mysql.connector
import json



app = flask.Flask(__name__)

conn=mysql.connector.connect(user="root",password="plokijuh9",database="j")#连接数据库，创建Flask_app数据库
cursor=conn.cursor()


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/search/',methods=['POST'])
def search():
    # Gene 是前端传回的 genes的值
    Gene = flask.request.values['genes']
    # 编写查询语言
    sql= "select * FROM illuminamethyl450_hg19_gpl16304_tcgalegacy where gene LIKE '%" + Gene + "%'"
    # 执行查询语言
    cursor.execute(sql)
    # 获取结果
    result = cursor.fetchall()
    # 查询结果条数
    number="select COUNT(id) FROM illuminamethyl450_hg19_gpl16304_tcgalegacy where gene LIKE '%" + Gene + "%'"
    # 执行条数查询
    cursor.execute(number)
    num = cursor.fetchall()
    nb=num[0]
    n=nb[0]

    sb = [result,n]

    return json.dumps(sb)

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
