# coding: utf-8
from mcpi.minecraft import Minecraft
import random
import time 
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = mc.getBlock(x, y, z)
mc.postToChat(blockType == 0)
height = 2
blockType = 1
sideHeight = height
pointHeight = 4
baseHeight = 1
time.sleep(5)
y = pos.y
mc.player.setPos(x, y + 10, z)
for i in range(150):        
    blockType = i
    mc.postToChat(i)
    # random.randint(0, 350)
    time.sleep(0.5)
    mc.setBlocks(x + i, y, z, x + i, y - 1, z + 4, blockType)
