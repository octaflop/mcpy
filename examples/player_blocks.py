# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import mcpi.block as block

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x, y, z = mc.player.getTilePos()
    b = mc.getBlock(x, y-1, z)
    mc.postToChat("Standing on: {}".format(b))
    time.sleep(2)
