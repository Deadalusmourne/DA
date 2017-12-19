#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/12/7 
# __author__: caoge
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4j83jf83d#4@vc'

    @staticmethod
    def init_app(app):
        pass


class AppConfig(Config):
    DEBUG = True


config = {
    'configa': AppConfig,
    'default': AppConfig
}

DB_CHOICE = {
    0: 'logic'
}