# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from invoke import ctask as task
import webbrowser


@task
def docs(ctx):
    ctx.run("sphinx-autobuild docs docs/_build/html/ -p 8001")
    webbrowser.open("http://127.0.0.1:8001")
