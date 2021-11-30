#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import hashids
import requests

from app.core.config import settings


class EncryptionHashIds(object):

    @property
    def __hashids(self):
        return hashids.Hashids(min_length=16)

    def encode(self, old_id):
        return self.__hashids.encode(old_id, 6666)

    def decode(self, h):
        try:
            return self.__hashids.decode(h)[0]
        except IndexError:
            return None


def wechat_login(code: str):
    """微信小程序登录"""
    result = requests.get(
        url="https://api.weixin.qq.com/sns/jscode2session",
        params={
            "appid": settings.APPID,
            "secret": settings.APP_SECRET,
            "js_code": code,
            "grant_type": "authorization_code"
        },
    ).json()
    return result


encrypt = EncryptionHashIds()


if __name__ == '__main__':
    i = 1
    e = EncryptionHashIds()
    r = e.encode(i)
    d = e.decode(r)
