# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from invoke import ctask as task
import webbrowser

import git
import os

# Get working directory
REL = os.path.dirname(os.path.realpath(__file__))
BUILD_PATH = os.path.join(REL, "mcbuild")


@task
def docs(ctx):
    """
    Compiles and starts up a docs server
    """
    os.chdir("docs")
    ctx.run("make html")
    os.chdir(REL)
    ctx.run("sphinx-autobuild docs docs/_build/html/ -p 8001")
    webbrowser.open("http://127.0.0.1:8001")


@task
def get_build_tools(ctx):
    """
    Main installation of build tools & Minecraft Python server
    """
    ctx.run("mkdir mcbuild; wget -O mcbuild/BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar")
    os.chdir("mcbuild")
    ctx.run("java -jar BuildTools.jar")
    os.chdir("/tmp")
    ctx.run("wget -O lpm.zip https://sourceforge.net/projects/python-with-minecraft-mac/files/latest/download")
    ctx.run("unzip lpm.zip -d lpm")
    ctx.run("rsync -rltvh --progress /tmp/lpm/MinecraftTools/server/ {}/".format(BUILD_PATH))

@task
def clean_build_tools(ctx):
    """
    Removes the mcbuild folder
    """
    os.chdir(REL)
    ctx.run("rm -rvf mcbuild/")


@task
def start_server(ctx):
    """
    Starts the Minecraft Python server
    """
    os.chdir("mcbuild")
    ctx.run("java -jar craftbukkit-1.8.8.jar")

