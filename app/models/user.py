#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用户相关的表信息
"""
from datetime import datetime
import enum

from sqlalchemy import Column, Integer, String, DateTime, Boolean, SmallInteger

from app.db.base_class import Base


class UnitEnum(enum.Enum):
    KG = 1  # 千克
    G = 2  # 克
    ML = 3  # 毫升
    L = 4  # 升
    unit = 5  # 个


class User(Base):
    """用户模型"""
    id = Column(Integer, primary_key=True)
    openid = Column(String, comment="微信用户在此小程序中的openid")
    session_key = Column(String, comment="用户的session_key")
    created_at = Column(DateTime, default=datetime.now, comment="注册时间")


class UserFoodstuff(Base):
    """用户的食材表"""
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, comment="用户的id")
    stuff_id = Column(Integer, comment="食材的id")
    name = Column(String, comment="食材的名称")
    icon = Column(String, comment="食材的icon")
    species = Column(SmallInteger, comment="食材类别：(1,蔬菜)、(2,肉)、(3,调料)")
    created_at = Column(DateTime, default=datetime.now, comment="添加时间")
    expire_date = Column(DateTime, comment="过期时间")
    total_amount = Column(Integer, comment="本次购买的食材总数")
    amount = Column(Integer, comment="食材剩余数量")
    unit = Column(Integer, comment="食材单位")
    status = Column(Boolean, comment="是否用完")
    storage_method = Column(Integer, comment="存储方式，(1,冷藏),(2,冷冻),(3,阴凉干燥)")
    remark = Column(String, comment="备注")


class UsageRecord(Base):
    """食材使用记录"""
    id = Column(Integer, primary_key=True)
    handler_date = Column(DateTime, comment="处理时间")
    remark = Column(DateTime, comment="备注")


class FoodstuffUsageRecord(Base):
    """食材使用记录"""
    id = Column(Integer, primary_key=True)
    uf_id = Column(Integer, comment="食材id")
    handler_date = Column(DateTime, comment="处理时间")
    use_for = Column(Integer, comment="用在哪里，关联usage_record表中的id，0：丢弃")
    amount = Column(Integer, comment="使用量")
