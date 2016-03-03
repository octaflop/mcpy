# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mcpi.block as block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


"""
Use a function to capture 
"""


def build_a_rainbow_tower(height, colors, offset=0):
    position = mc.player.getTilePos()
    x, y, z = position.x, position.y, position.z
    mc.player.setTilePos(x, y, z)
    col_index = 0
    for color in colors:
        for pos in range(0, height):
            pos += col_index
            mc.setBlock(x + offset, y + pos, z, block.WOOL.id, color)
        col_index += height 

normal_colors = [14, 1, 4, 5, 3, 11, 10]
normal_height = 5
build_a_rainbow_tower(normal_height, normal_colors)

crazy_colors = [5, 5, 3, 11, 10, 14, 4, 1]
crazy_height = 16
build_a_rainbow_tower(crazy_height, crazy_colors, 5)
