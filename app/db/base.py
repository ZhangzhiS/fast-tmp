#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import *  # noqa
from app.models.food import *  # noqa
