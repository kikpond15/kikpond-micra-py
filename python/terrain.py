def setFloor(mc, width=25, depth=25,block_id = 2):
    p = mc.player.getTilePos()
    mc.postToChat("start set floor")
    for x in range(width):
        for z in range(depth):
            mc.setBlock(p.x+x, p.y, p.z+z, block_id)
            mc.setBlock(p.x-x, p.y, p.z+z, block_id)
            mc.setBlock(p.x+x, p.y, p.z-z, block_id)
            mc.setBlock(p.x-x, p.y, p.z-z, block_id)
    mc.postToChat("end set floor")


def leveling(mc, width=25, height=25, depth=25):
    block_id = 0
    p = mc.player.getTilePos()
    mc.postToChat("start leveling")
    for y in range(height):
        for x in range(width):
            for z in range(depth):
                mc.setBlock(p.x+x, p.y+height-y, p.z+z, block_id)
                mc.setBlock(p.x-x, p.y+height-y, p.z+z, block_id)
                mc.setBlock(p.x+x, p.y+height-y, p.z-z, block_id)
                mc.setBlock(p.x-x, p.y+height-y, p.z-z, block_id)
    mc.postToChat("end set floor")


def drawAxis(mc, block_num = 25):
    p = mc.player.getTilePos()
    mc.postToChat("start draw axis")
    for num in range(block_num):
        mc.setBlock(p.x+num, p.y, p.z, 35, 14)
        mc.setBlock(p.x, p.y, p.z+num, 35, 11)
    mc.postToChat("end draw axis")

if __name__ == '__main__':
    leveling()
    
