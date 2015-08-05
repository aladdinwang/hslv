# coding: utf-8

from functools import wraps

from flask import g, jsonify

def register_request_callbacks(callbacks):
    def _wrapper(f):
        def _inner(*args, **kwargs):
            path = f.__module__.rsplit('.', 1)
