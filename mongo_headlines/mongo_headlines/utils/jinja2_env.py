#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: rentao
# @Time: 2022/5/22 7:04

from jinja2.environment import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

"""
下面的设置主要是为了能在 jinja2 的模板中能够使用 {{ url('') }} {{ static('') }} 这种类型的语句
"""


def environment(**options):
    """
    设置jinja2模板的环境变量
    :param options:
    :return:
    """
    env = Environment(**options)
    env.globals.update({
        "static": staticfiles_storage.url,
        "url": reverse
    })
    return env
