# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from math import sin, pi

import mcpi.block as block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


"""
A simple rainbow script

Inspired by: http://www.minecraftforum.net/forums/other-platforms/minecraft-pi-edition/1959851-my-first-script-for-minecraft-pi-api-a-rainbow
"""

colors = [14, 1, 4, 5, 3, 11, 10]
height = 30

# unpack player position
x, z, y = mc.player.getPos()
mc.setBlocks(-64+x, y, z, 64+x, height + len(colors)+y, z, 0)
for x in range(0, 128):
    for ci in range(0, len(colors)):
        y = sin((x / 128.0) * pi) * height + ci
        mc.setBlock(x - 64, y, 0, block.WOOL.id, colors[len(colors) - 1 - ci])