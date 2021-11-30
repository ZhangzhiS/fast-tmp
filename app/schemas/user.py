#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Any


class UserCreate(UserBase):
    openid: str
    session_key: str
    created_at: Optional[datetime]


class UserUpdate(UserBase):
    pass


class UserInDbBase(UserBase):

    class Config:
        orm_mode = True


class LoginResponseUser(UserInDbBase):
    id: str
