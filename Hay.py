import Water
import Fertilizer
import Hat

def Hay(hay_amount):
	clear()
	def harvestROW():
		for _ in range(get_world_size()):
			Water.Water()
			Fertilizer.Fertilizer()
			if can_harvest():
				harvest()
			move(North)

	while num_items(Items.Hay) <= hay_amount:
		if spawn_drone(harvestROW):
			move(East)
	