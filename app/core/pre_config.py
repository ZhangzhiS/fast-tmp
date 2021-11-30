# -*- coding: utf-8 -*-
from typing import List
from pydantic import BaseModel, validator


class StorageMethod(BaseModel):
    """食物存储方式"""
    method: str
    code: int


class Unit(BaseModel):
    """预设单位"""
    name: str
    code: int


pre_storage_method = {
    1: "冷藏",
    2: "冷冻",
    3: "阴凉干燥",
}

storage_method_colors = {
    1: "blue",
    2: "green",
    3: "orange",
}

pre_unit = {
    1: "kg",
    2: "g",
    3: "ml",
    4: "l",
    5: "个"
}

freshness_colors = {}


class AppConfig(BaseModel):
    """app的一些常量配置"""

    storage_method_config: List[StorageMethod] = [
        StorageMethod(method=v, code=k) for k, v in pre_storage_method.items()
    ]
    unit_config: List[Unit] = [
        Unit(name=v, code=k) for k, v in pre_unit.items()
    ]


app_config = AppConfig()
