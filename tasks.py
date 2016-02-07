# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from invoke import ctask as task
import webbrowser


@task
def docs(ctx):
    ctx.run("sphinx-autobuild docs docs/_build/html/ -p 8001")
    webbrowser.open("http://127.0.0.1:8001")


@task
def get_build_tools(ctx):
    ctx.run("wget -O mcbuild/BuildTools https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar")
    ctx.run("cd mcbuild && java -jar BuildTools.jar")
