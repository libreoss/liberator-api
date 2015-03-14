#!/usr/bin/env python

from setuptools import setup

setup(
    name='liberator-api',
    version='0.1',
    description='Liberator API',
    author='Goran Mekić',
    author_email='meka@lugons.org',
    url='https://github.com/libreoss/liberator-api',
    packages=[
        'liberator',
        'liberator.models',
        'liberator.serializers',
        'liberator.fixtures',
        'liberator.views',
    ],
    install_requires=[
        'django',
        'django-cors-headers',
        'djangorestframework',
        'djangorestframework-jwt',
        'psycopg2',
    ]
)
