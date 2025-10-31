import Hat

def Maze(Gold_amount):
	directions = [North, East, South, West]
	index = 0
	
	def resetMaze():
		while(get_pos_x() != 0):
			move(West)
		while(get_pos_y() != 0):
			move(North)
		harvest()
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
	
	def runMaze(index):
		while True:
			if(num_drones() < max_drones()):
				spawn_drone(spawnDrone)
			if(get_entity_type() == Entities.Treasure):
				harvest()
				resetMaze()
				return
			if not move(directions[index]):
				index = (index + 1) % 4
			else:
				index = (index - 1) % 4
			
	def runMazeReverse(index):
		while True:
			if(num_drones() < max_drones()):
				spawn_drone(spawnDrone)
			if(get_entity_type() == Entities.Treasure):
				harvest()
				resetMaze()
				return
			if not move(directions[index]):
				index = (index - 1) % 4
			else:
				index = (index + 1) % 4
				
	def spawnDrone():
		do_a_flip()	
		Hat.Changehat()
		runMazeReverse(0)
		
	if((get_entity_type() != Entities.Hedge) and (get_entity_type() != Entities.Treasure)):
		resetMaze()
		
	while num_items(Items.Gold) <= Gold_amount:
		runMaze(index)