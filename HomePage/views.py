# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')