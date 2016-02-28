# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""
A very basic tower.
Teaches fundamentals of block placement.
"""

position = mc.player.getTilePos()
x, y, z = position.x, position.y, position.z

mc.player.setTilePos(x, y, z)

for b in range(-5, 20):
    mc.setBlock(x, y + b, z, 103)
