while True:
	clear()
	upgrades = []
	for i in Unlocks:
		if get_cost(i) != {}:
			for item in get_cost(i):
				index = 0
				if num_items(item) >= get_cost(i)[item]:
					index += 1
				if index == len(get_cost(i)):
					unlock(i)
			upgrades.append(i)
	
	priority = []
	for i in range(len(upgrades)):
		Acost = get_cost(upgrades[i])
		#if it's already at max lvl
		if Acost == {}:
			priority.insert(i,0)
		else:
			priority.insert(i,1)
		#'Tier' of upgrade {More Dependancy the lower the priority}
		for item in Acost:
			if item == Items.Cactus: # Tier 4
				priority[i] += 1
			if item == Items.Pumpkin: # Tier 3
				priority[i] += 2
			if item == Items.Carrot: #Tier 2
				priority[i] += 3
			if item == Items.Wood: # Tier 1
				priority[i] += 4
			if item == Items.Hay: # Tier 1
				priority[i] += 4
			if item == Items.Gold: # Tier 2
				priority[i] += 3
			if item == Items.Weird_Substance: # Tier 1
				priority[i] += 4
			if item == Items.Bone: # Tier 5
				priority[i] -= 1
			
		#Upgrades' current lvl relative to it's max lvl {The closer to max; the lower the priority}
		maxlvl = 0 
		while get_cost(upgrades[i],maxlvl) != {}:
			maxlvl += 1
		priority[i] -= (num_unlocked(upgrades[i])//maxlvl) * 10
		
		#The Amount of different items 
		priority[i] /= len(Acost)
		
		for item in Acost:
			if Acost[item] >= 100000:
				priority[i] -= (Acost[item]//1000000)
			if Acost[item] >= 10000:
				priority[i] -= (Acost[item]//100000)//2
			if Acost[item] >= 1000:
				priority[i] -= (Acost[item]//1000000)//10
				
			
	for i in range(len(priority)):
		if priority[i] == max(priority):
			maxpriority = i
		
	print(upgrades[maxpriority])
		
	cost = get_cost(upgrades[maxpriority])
	
	
	for item in cost:
		if item == Items.Bone:
			import Dinosaur
			Dinosaur.Dinosaur(cost[item])
		if item == Items.Cactus:
			import Cactus
			Cactus.Cactus(cost[item])
		if item == Items.Pumpkin:
			import Pumpkin
			Pumpkin.Pumpkin(cost[item])
		if item == Items.Carrot:
			import Carrot
			Carrot.Carrot(cost[item])
		if item == Items.Wood:
			import Tree
			Tree.Tree(cost[item])
		if item == Items.Hay:
			import Hay
			Hay.Hay(cost[item])
		if item == Items.Gold:
			import Maze
			Maze.Maze(cost[item])
	unlock(upgrades[maxpriority])
		