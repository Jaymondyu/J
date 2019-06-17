#encoding: utf-8

# 模板
#     用来快速生成html页面
#     静态html

    # 模板语法
    #     变量
    #         {{ var }}
    #         视图传递给模板的数据
    #         前面定义出来的数据
    #         变量不存在,默认忽略
    #     标签
    #         {% tag %}
    #         控制逻辑
    #         使用外部表达式
    #         创建变量
    #         宏定义


    # 结构标签
    #     block
    #         {% block XXX %}
    #         {% endblock%}
    #         规划性标签
    #         首次出现挖坑
    #         非首次出现填坑
    #         多次填坑会出现覆盖,不想覆盖就用{{super()}}
    #
    #     extends
    #         {% extends 'XXX'%}
    #
    #         继承后保留块中的内容
    #         {{ super() }}
    #
    #     挖坑继承体现的是化整为零的操作

        # include
        #     {% include 'xxx' %}
        #     包含,将其他html包含近来,体现的是由零到一的概念
        #     能用block+extend实现的,就尽量别用include
        #
        # marco
        #     {% marco hello(name) %}
        #             {{ name }}
        #     {% endmarco %}
        #     宏定义,可以在模板中定义函数,在其他地方调用
        #     可以接受参数
        #     通过调用函数生成html
        #     支持导入操作

        # 宏定义可导入
        #     {% from 'xxx' import xxx %}

        # 过滤器
            # {{ var|过滤器|过滤器 }}
            # 过滤器并不是先写先执行
            # safe其实总是会最后做的





from flask import Flask,session
from App.views import blue


app=Flask(__name__)

#设置secret key
app.config['SECRET_KEY'] = "plokijuh9"


app.register_blueprint(blueprint=blue)


if __name__=='__main__':
    app.run(debug=True,port=3001)
