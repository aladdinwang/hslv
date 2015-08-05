# coding: utf-8

from . import error_codes


class CommonException(Exception):
    status_code = 200
    error_code = error_codes.COMMON_ERROR

    def __init__(self, message, status_code=None, error_code=None, payload=None):
        self.message = message

        if status_code:
            self.status_code = status_code
        if error_code:
            self.error_code = error_code
        self.payload = payload


    def to_dict(self):
        d = dict(self.payload or ())
        d['message'] = self.message
        d['code'] = self.error_code
        return d


class APIError(CommonException):
    pass
