# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:59:19 2020

@author: itcadmin
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'