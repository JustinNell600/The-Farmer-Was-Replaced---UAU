import Water
import Fertilizer
import Hat

def Tree(Wood_amount):
	clear()
	def harvestROW():
		Hat.Changehat()	
		for _ in range(get_world_size()):
			Water.Water()
			Fertilizer.Fertilizer()
			if can_harvest():
				harvest()
			if (get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 1):
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(East)
	
	while num_items(Items.Wood) <= Wood_amount:
		if spawn_drone(harvestROW):
			move(North)
		
	