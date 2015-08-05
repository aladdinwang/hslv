# coding: utf-8

import importlib
import json

from flask import Flask, Blueprint, jsonify, render_template

from core.exceptions import APIError


app = Flask(__name__)
app.debug = True
#加栽配置
app.config.from_object('default_settings')

#加载模块
for app_ in app.config.get('APPS') or []:
    m = importlib.import_module(app_)
    if hasattr(m, 'bp'):
        app.register_blueprint(m.bp)

#出错处理
@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(404)
def handle_404(error):
    return render_template('user/not_found.html')




if '__main__' == __name__:
    print app.url_map
    app.run(host='0.0.0.0')
