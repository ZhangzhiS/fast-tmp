#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_openid(self, db: Session, openid: str) -> Optional[User]:
        return db.query(self.model).filter(
            self.model.openid == openid
        ).first()


user_crud = CRUDUser(User)
