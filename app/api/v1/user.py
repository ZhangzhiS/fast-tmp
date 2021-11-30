#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.schemas.user import LoginResponseUser
from app.api import deps
from app.controller import user
from app.utils import encrypt

user_route = APIRouter()


class Code(BaseModel):
    code: str


@user_route.post("/login")
def login(
        *,
        db: Session = Depends(deps.get_db),
        code: Code = Body(None)
):
    """
    微信小程序获取登录，获取用户openid
    """
    result = user.get_user_info(code.code, db)
    result.id = encrypt.encode(result.id)
    data = result.as_dict(exclude={"session_key"})
    # data.pop("session_key")
    return deps.write_success(data=data, data_type_same=False)
