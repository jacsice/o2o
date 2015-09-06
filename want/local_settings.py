#!/usr/bin/python
# -*- coding:utf-8 -*-

DEBUG = True

TEMPLATE_DEBUG = DEBUG

LANGUAGE_CODE = 'zh-cn'

SERVER_URL = 'http://jacsice.ngrok.com'
SERVER_TOKEN = 'want'
SERVER_ID = 'gh_33016337c2e2'

APP_ID = 'wx88c30f037ed63a21'
APP_SECRET = 'e99b0fc16b49c82e82649e7c4f1f6589'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'want',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
