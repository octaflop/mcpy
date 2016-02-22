# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mcpi.block as block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
area = 28
blockid = block.GLASS.id

mc.postToChat("setting blocks")
mc.setBlocks(x+1, y+1, z+1, x+area, y+area, z+area, blockid)
