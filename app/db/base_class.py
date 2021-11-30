#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

    def as_dict(self, exclude=None) -> dict:
        if exclude is None:
            exclude = {}
        res = dict()
        for c in inspect(self).mapper.column_attrs:
            if c.key in exclude:
                continue
            if isinstance(getattr(self, c.key), datetime):
                res[c.key] = getattr(self, c.key).strftime("%Y-%m-%d")
            else:
                res[c.key] = getattr(self, c.key)
        # return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs if c.key not in exclude}
        return res
