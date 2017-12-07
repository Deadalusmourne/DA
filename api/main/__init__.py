#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/12/7 
# __author__: caoge

from flask import Blueprint

main = Blueprint("main", __name__)
from . import views