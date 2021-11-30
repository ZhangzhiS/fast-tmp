#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用户相关的操作
"""
import requests

from app import crud, utils
from app.core import err
from app.schemas.user import UserCreate


def get_user_info(code: str, db):
    """
    从微信服务器获取用户信息
    :param db: 数据库连接
    :param code: 前端传的code
    :return: 返回用户信息
    """
    result = utils.wechat_login(code)
    if not result.get("openid"):
        raise err.WxLoginError(data=result)
    openid = result.get("openid")
    user = crud.user_crud.get_by_openid(db, openid)
    if user:
        return user
    return crud.user_crud.create(
        db, obj_in=UserCreate(
            openid=openid,
            session_key=result.get("session_key"),
        )
    )
