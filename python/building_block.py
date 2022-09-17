from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import terrain

mc.player.setTilePos(0, 0, 0)
terrain.leveling(mc, 25, 20, 25)
terrain.setFloor(mc, 25, 25, 98)
terrain.drawAxis(mc, 25)
