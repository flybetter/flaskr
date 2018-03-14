#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= flask_demo
@file= setup
@author= wubingyu
@create_time= 2018/3/13 下午4:44
"""
from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)