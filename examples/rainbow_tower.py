# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mcpi.block as block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

colors = [14, 1, 4, 5, 3, 11, 10]
color_height = 5

"""
Using a loop for colors and a loop for color height, create a tower of rainbow blocks
"""

position = mc.player.getTilePos()
x, y, z = position.x, position.y, position.z

mc.player.setTilePos(x, y, z)

col_index = 0
for color in colors:
    for pos in range(0, color_height):
        pos += col_index
        mc.setBlock(x, y + pos, z, block.WOOL.id, color)
    col_index += color_height 
