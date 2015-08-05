# coding: utf-8

from flask import abort, g, render_template

from core.exceptions import APIError

from . import bp


@bp.route('/', defaults={'page': 'index'})
@bp.route('/<page>')
def test(page):
    abort(404)
    return render_template('user/index.html')
    print dir(g)
    raise APIError('测试异常处理')
    return page





print type(test.__module__), test.__module__
print locals()
