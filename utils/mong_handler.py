#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/12/7 
# __author__: caoge
import pymongo
import bson
import config

client = pymongo.MongoClient(config.MONGO_HOST, config.MONGO_PORT, connect=False)

def get_db_by_name(db_name):
    if db_name:
        return client[db_name]
    else:
        return None

def get_collection(db_name,table_name):
    db = get_db_by_name(db_name)
    if db and table_name:
        collection = db[table_name]
    else:
        collection = None
    return collection