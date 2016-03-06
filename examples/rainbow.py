# -*- coding: utf-8 -*-
"""A simple rainbow script
Inspired by:
http://www.minecraftforum.net/forums/other-platforms/minecraft-pi-edition/1959851-my-first-script-for-minecraft-pi-api-a-rainbow
"""
from __future__ import unicode_literals
from math import sin, pi

from mcpi import block
from mcpi.minecraft import Minecraft


RED = 14
ORANGE = 1
YELLOW = 4
LIME = 5
LIGHT_BLUE = 3
BLUE = 11
PURPLE = 10
COLORS = (RED, ORANGE, YELLOW, LIME, LIGHT_BLUE, BLUE, PURPLE)
RAINBOW_HEIGHT = 60
RAINBOW_WIDTH = 128
RAINBOW_HALF = RAINBOW_WIDTH / 2

mc = Minecraft.create()
# unpack player position
position = mc.player.getTilePos()
px, py, pz = position.x, position.y, position.z

for curve_x in range(0, RAINBOW_WIDTH):
    curve = sin(pi * float(curve_x) / float(RAINBOW_WIDTH)) * RAINBOW_HEIGHT
    for color in COLORS:
        map_pos_y = int(curve) - COLORS.index(color)
        mc.setBlock(
            curve_x - RAINBOW_HALF + px, map_pos_y + py, pz,
            block.WOOL.id,
            color)
