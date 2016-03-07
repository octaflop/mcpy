# -*- coding: utf-8 -*-
"""
http://www.raspberrypi-spy.co.uk/2014/06/building-a-castle-in-minecraft-with-python/
--------------------------------------
    Minecraft Python API
       Castle Builder

This script creates a castle complete
with moat and perimeter walls.

Author : Matt Hawkins
Date   : 07/06/2014

http://www.raspberrypi-spy.co.uk/
--------------------------------------
"""
from __future__ import unicode_literals
import time

from mcpi import block
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3


def clear_landscape(ctr, moat_depth, clear_height, clear_dist):
    # Set lower half of world to dirt
    mc.setBlocks(ctr.x - clear_dist, -1, ctr.z - clear_dist,
                 ctr.x - clear_dist, -moat_depth - 1, ctr.z - clear_dist,
                 block.DIRT)
    # add a layer of grass
    mc.setBlocks(ctr.x - clear_dist, 0, ctr.z - clear_dist,
                 ctr.x + clear_dist, 0, ctr.z + clear_dist,
                 block.GRASS)
    # Set upper half to air
    mc.setBlocks(ctr.x - clear_dist, 1, ctr.z - clear_dist,
                 ctr.x + clear_dist, clear_height, ctr.z + clear_dist,
                 block.AIR)


def create_landscape(ctr, moatwidth, moatdepth, islandwidth, base_height):
    # Create water moat
    mc.setBlocks(ctr.x - moatwidth, 0, ctr.z - moatwidth,
                 ctr.x + moatwidth, -moatdepth, ctr.z + moatwidth,
                 block.WATER)
    # Create island inside moat
    mc.setBlocks(ctr.x - islandwidth, 0, ctr.z - islandwidth,
                 ctr.x + islandwidth, base_height, ctr.z + islandwidth,
                 block.GRASS)


def create_walls(ctr, size, baseheight, height, material, corners):
    cnr_sz = 0
    if corners:
        cnr_sz = 2
    # Create 4 walls with a specified width, height and material.
    mc.setBlocks(
        ctr.x - size + cnr_sz, baseheight + 1, ctr.z - size,
        ctr.x + size - cnr_sz, baseheight + height, ctr.z - size,
        material)
    mc.setBlocks(
        ctr.x - size, baseheight + 1, ctr.z - size + cnr_sz,
        ctr.x - size, baseheight + height, ctr.z + size - cnr_sz,
        material)
    mc.setBlocks(
        ctr.x + size - cnr_sz, baseheight + 1, ctr.z + size,
        ctr.x - size + cnr_sz, baseheight + height, ctr.z + size,
        material)
    mc.setBlocks(
        ctr.x + size, baseheight + 1, ctr.z + size - cnr_sz,
        ctr.x + size, baseheight + height, ctr.z - size + cnr_sz,
        material)

    if corners:
        corner = Vec3(ctr.x - size, 0, ctr.z - size)
        create_walls(corner, 2, baseheight, height, material, False)
        corner = Vec3(ctr.x + size, 0, ctr.z + size)
        create_walls(corner, 2, baseheight, height, material, False)
        corner = Vec3(ctr.x + size, 0, ctr.z - size)
        create_walls(corner, 2, baseheight, height, material, False)
        corner = Vec3(ctr.x - size, 0, ctr.z + size)
        create_walls(corner, 2, baseheight, height, material, False)
        # clear the overlap
        create_walls(ctr, size - 1, baseheight, height, block.AIR, False)
        create_walls(ctr, size - 2, baseheight, height, block.AIR, False)

    # Add battlements to top edge
    for x in range(cnr_sz, (2 * size) + 1 - cnr_sz, 2):
        # positive x, z changes
        mc.setBlock(ctr.x + size, baseheight + height + 1, ctr.z + x - size,
                    material)
        # negative x, z changes
        mc.setBlock(ctr.x - size, baseheight + height + 1, ctr.z + x - size,
                    material)
        # positive z, x changes
        mc.setBlock(ctr.x + x - size, baseheight + height + 1, ctr.z + size,
                    material)
        # negative z, x changes
        mc.setBlock(ctr.x + x - size, baseheight + height + 1, ctr.z - size,
                    material)

    if material != block.AIR:
        # Add wooden walkways
        mc.setBlocks(
            ctr.x - size + 1, baseheight + height - 1, ctr.z + size - 1,
            ctr.x + size - 1, baseheight + height - 1, ctr.z + size - 2,
            block.WOOD_PLANKS)
        mc.setBlocks(
            ctr.x - size + 1, baseheight + height - 1, ctr.z - size + 1,
            ctr.x + size - 1, baseheight + height - 1, ctr.z - size + 2,
            block.WOOD_PLANKS)
        mc.setBlocks(
            ctr.x - size + 1, baseheight + height - 1, ctr.z - size + 1,
            ctr.x - size + 2, baseheight + height - 1, ctr.z + size - 1,
            block.WOOD_PLANKS)
        mc.setBlocks(
            ctr.x + size - 1, baseheight + height - 1, ctr.z - size + 1,
            ctr.x + size - 2, baseheight + height - 1, ctr.z + size - 1,
            block.WOOD_PLANKS)


def create_windows(x, y, z, direction):
    if direction in ('N', 'S'):
        z1 = z
        z2 = z
        x1 = x - 2
        x2 = x + 2
    elif direction in ('E', 'W'):
        z1 = z - 2
        z2 = z + 2
        x1 = x
        x2 = x

    mc.setBlocks(x1, y, z1, x1, y + 1, z1, block.AIR)
    mc.setBlocks(x2, y, z2, x2, y + 1, z2, block.AIR)

    if direction == "N":
        a = 3
    elif direction == "S":
        a = 2
    elif direction == "W":
        a = 0
    else: # direction == "E":
        a = 1

    mc.setBlock(x1, y - 1, z1, 109, a)
    mc.setBlock(x2, y - 1, z2, 109, a)


def create_keep(ctr, size, baseheight, levels, material):
    # Create a keep with a specified number
    # of floors levels and a roof
    height = (levels * 5) + 5

    create_walls(ctr, size, baseheight, height, material, False)

    # Floors & Windows
    for level in range(1, levels + 1):
        level_height = baseheight + (level - 1) * 5
        if level > 1:
            # Floors
            mc.setBlocks(ctr.x - size + 1, level_height, ctr.z - size + 1,
                         ctr.x + size - 1, level_height, ctr.z + size - 1,
                         block.WOOD_PLANKS)

            # Windows
            create_windows(ctr.x, level_height + 2, ctr.z + size, "N")
            create_windows(ctr.x, level_height + 2, ctr.z - size, "S")
            create_windows(ctr.x - size, level_height + 2, ctr.z, "W")
            create_windows(ctr.x + size, level_height + 2, ctr.z, "E")

    # Door
    mc.setBlocks(ctr.x, baseheight + 1, ctr.z + size,
                 ctr.x, baseheight + 2, ctr.z + size,
                 block.AIR)


if __name__ == '__main__':
    mc = Minecraft.create()
    mc.postToChat("Let's build a castle!")

    mc.postToChat('Clearing the landscape')
    MOAT_DEPTH = 10
    CLEAR_HEIGHT = 40
    CLEAR_DIST_FROM_CENTER = 35
    center = mc.player.get_tile_pos()
    clear_landscape(center, MOAT_DEPTH, CLEAR_HEIGHT, CLEAR_DIST_FROM_CENTER)
    time.sleep(2)

    mc.postToChat("Create ground and moat")
    MOAT_WIDTH = 33
    ISLAND_WIDTH = 23
    BASE_HEIGHT = 1
    create_landscape(center, MOAT_WIDTH, MOAT_DEPTH, ISLAND_WIDTH, BASE_HEIGHT)
    time.sleep(2)

    mc.postToChat("Create outer walls")
    OUTER_WALL_SIZE = 21
    OUTER_WALL_HEIGHT = 8
    CASTLE_MATERIAL = block.MOSS_STONE
    create_walls(center, OUTER_WALL_SIZE, BASE_HEIGHT, OUTER_WALL_HEIGHT,
                 CASTLE_MATERIAL, True)
    time.sleep(2)

    mc.postToChat("Create inner walls")
    INNER_WALL_SIZE = 13
    INNER_WALL_HEIGHT = 16
    create_walls(center, INNER_WALL_SIZE, BASE_HEIGHT, INNER_WALL_HEIGHT,
                 CASTLE_MATERIAL, True)
    time.sleep(2)

    KEEP_LEVELS = 6
    mc.postToChat("Create Keep with %d levels" % KEEP_LEVELS)
    KEEP_SIZE = 5
    create_keep(center, KEEP_SIZE, BASE_HEIGHT, KEEP_LEVELS, CASTLE_MATERIAL)
    time.sleep(2)

    PLAYER_POSITION = 1
    if PLAYER_POSITION == 1:
        # outside of castle
        mc.player.setPos(center.x + CLEAR_DIST_FROM_CENTER - 1,
                         BASE_HEIGHT + 1, center.z)
    elif PLAYER_POSITION == 2:
        # inside keep
        mc.player.setPos(center.x, BASE_HEIGHT + 1, center.z)
    elif PLAYER_POSITION == 3:
        # outer wall walkway
        mc.player.setPos(center.x + OUTER_WALL_SIZE - 1,
                         OUTER_WALL_HEIGHT + BASE_HEIGHT,
                         center.z)
    elif PLAYER_POSITION == 4:
        # inner wall walkway
        mc.player.setPos(center.x + INNER_WALL_SIZE - 1,
                         INNER_WALL_HEIGHT + BASE_HEIGHT,
                         center.z)
    elif PLAYER_POSITION == 5:
        # atop keep
        mc.postToChat("Position player on Keep's walkway")
        PLAYER_Y = KEEP_LEVELS * 5 + 6 + BASE_HEIGHT
        PLAYER_Z = KEEP_SIZE - 1
        mc.player.setPos(center.x, PLAYER_Y, center.z + PLAYER_Z)
