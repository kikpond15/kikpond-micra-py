def leveling(mc, block_id=2):
    p = mc.player.getTilePos()
    mc.postToChat("start leveling")
    num = 20
    for i in range(num):
        for j in range(num):
            mc.setBlock(p.x-(num/2)+i, p.y-1, p.z-(num/2)+j, block_id)
    mc.postToChat("end leveling")


if __name__ == '__main__':
    leveling()
