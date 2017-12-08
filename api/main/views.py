#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/12/7 
# __author__: caoge
from flask import request, jsonify
from . import main
import config
from utils import mong_handler

@main.route('/', methods=['GET', 'POST'])
def index():
    return 'hello world'

@main.route('/write_row_data', methods=['POST'])
def write_row_data():
    post_param = request.json() or {}
    db_type = post_param['db_type']
    data = post_param['data']
    db_name = config.DB_CHOICE[db_type]
    coll_name = post_param['coll_name']
    coll = mong_handler.get_collection(db_name=db_name, table_name=coll_name)
    if isinstance(data, dict):
        data = [data, ]


@main.route('/fast_write', methods=['POST'])
def fast_write():
    req = {'success': 0, 'resp': {}, 'error': '', 'trace_back': ''}
    post_param = request.json() or {}
    try:
        db_type = post_param['db_type']
        data = post_param['data']
        db_name = config.DB_CHOICE[db_type]
        coll_name = post_param['coll_name']
    except KeyError as e:
        req['error'] = '参数错误'
        req['trace_back'] = e
        return jsonify(req)
    coll = mong_handler.get_collection(db_name=db_name, table_name=coll_name)
    if isinstance(data, dict):
        data = [data, ]
    result = coll.insert_many(data)
    ids_b = result.inserted_ids
    req_ids = [str(x) for x in ids_b]
    req['success'] = 1
    req['resp']['req_ids'] = req_ids
    return jsonify(req)