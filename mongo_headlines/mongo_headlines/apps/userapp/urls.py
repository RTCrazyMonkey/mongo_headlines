#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: rentao
# @Time: 2022/5/23 22:58

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^register/$', views.RegisterView.as_view()),
]

