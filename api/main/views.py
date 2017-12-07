#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/12/7 
# __author__: caoge

from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return 'hello world'