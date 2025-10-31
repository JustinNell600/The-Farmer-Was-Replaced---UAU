import Tree
import Hay
import Water
import Fertilizer
import Hat
import Cost

def Carrot(carrot_amount):
	Tree.Tree(Cost.Cost(carrot_amount,Items.Carrot))
	Hay.Hay(Cost.Cost(carrot_amount,Items.Carrot))
	clear()
	def harvestROW():
		Hat.Changehat()	
		for _ in range(get_world_size()):
			Water.Water()
			Fertilizer.Fertilizer()
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
			move(East)
			
	while num_items(Items.Carrot) <= carrot_amount:
		if spawn_drone(harvestROW):
			move(North)
		
	