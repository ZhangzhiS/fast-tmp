#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Generator, Any

from pydantic import BaseModel

from app.db.base_class import Base
from app.db.session import SessionLocal


def get_db(db: Any = None) -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def write_success(
    data: Any = None,
    code: int = 20000,
    msg: str = "success",
    data_type_same: bool = True
) -> dict:
    if not data:
        return {"data": None, "code": code, "msg": msg}
    if not isinstance(data, list):
        data = [data]
    res = [] if data_type_same else {}
    for i in data:
        if isinstance(i, dict):
            tmp = i
        elif isinstance(i, BaseModel):
            tmp = i.dict()
        elif isinstance(i, Base):
            tmp = i.as_dict()
        else:
            continue
        if data_type_same:
            res.append(tmp)
        else:
            res.update(tmp)
    return {"data": res, "code": code, "msg": msg}
