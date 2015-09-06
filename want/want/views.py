#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import logging
import decimal

from datetime import datetime, timedelta

from django.conf import settings
from django.db import transaction

from django.db import transaction
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("index")