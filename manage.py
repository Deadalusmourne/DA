#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/12/7 
# __author__: caoge
import os
from api import create_app
from flask_script import Manager, Shell, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))   # python3 manage.py shell 进入flask的shell环境
manager.add_command("run8080", Server(host="127.0.0.1", port=8080))

if __name__ == '__main__':
    manager.run()