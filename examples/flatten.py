# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

import mcpi.block as block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Flattening")
mc.setBlocks(-128,0,-128,128,64,128,0)
mc.setBlocks(-128,0,-128,128,-64,128,block.SANDSTONE.id)
mc.postToChat("Putting a diamond block at 0,0,0")
mc.setBlock(0,0,0,block.DIAMOND_BLOCK.id)

playerPos = mc.player.getPos()
msg = "Find your position - its x=%s z=%s y=%s" % (int(playerPos.x), int(playerPos.z), int(playerPos.y))
mc.postToChat(msg)
time.sleep(1)