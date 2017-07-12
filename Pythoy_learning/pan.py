#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-08 18:25:52
# @Author  : kris_jiang (kris_jiang@compal.com)
# @Link    : ${link}
# @Version : $1.0$

from flask import Flask
from flask import render_template  # 基于jinja2
from flask import request

app = Flask(__name__)


@app.route('/')  # /=定义的页面
def index():
    # 处理当前定义的这个页面的请求的响应
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files.get('file')
    filename = file.filename
    file.save('static/%s' % filename)
    return 'static/%s' % filename


if __name__ == '__main__':
    app.run(debug=True)

# tornade //高并发
