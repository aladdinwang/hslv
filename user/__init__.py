# coding: utf-8
from flask import Blueprint


bp = Blueprint('user', __name__, url_prefix='/user')


#注册试图
import apis
