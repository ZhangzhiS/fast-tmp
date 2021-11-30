#! /usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from app.core.config import settings


class BaseError(Exception):
    """异常基类"""

    def __init__(self, code: int, msg: str, data):
        self.code = code
        self.msg = msg
        self.data = data


class TestError(BaseError):
    """测试基类"""
    pass


class WxLoginError(BaseError):
    """微信登录接口异常"""

    def __init__(self, data):
        self.code = 40100
        self.msg = "微信登录接口异常"
        self.data = data


class UserIdError(BaseError):
    """用户id错误"""

    def __init__(self):
        self.code = 40000
        self.msg = "用户的id参数错误"
        self.data = None


class ParamsError(BaseError):
    """参数错误"""
    def __init__(self, param="参数"):
        self.code = 40001
        self.msg = "请求参数异常" if settings.DEBUG else f"{param}异常"
        self.data = None

