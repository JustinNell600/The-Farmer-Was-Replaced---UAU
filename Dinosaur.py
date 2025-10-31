import Cactus
import Cost
def Dinosaur(bone_amount):
	def run_dinosaur_game(farm_size, max_tiles, path):
		clear()
		change_hat(Hats.Dinosaur_Hat)
		
		success = True
		
		while success:
			for direction in path:
				success = move(direction)
		
		change_hat(Hats.Brown_Hat)
	
	
	def generate_looping_path(farm_size):
		path = []
		path.append(East)
		for row in range(farm_size):
			if row % 2 == 0:
				for col in range(farm_size - 2):
					path.append(East)
			else:
				for col in range(farm_size - 2):
					path.append(West)
			if row < farm_size - 1:
				path.append(North)
		path.append(West)
		for row in range(farm_size-1):
			path.append(South)
		
		return path
	
	
	def main():
		while num_items(Items.Bone) <= bone_amount:
			run_dinosaur_game(farm_size, max_tiles, path)
	
	farm_size = get_world_size()
	max_tiles = farm_size * farm_size
	path = generate_looping_path(farm_size)
	
	Cactus.Cactus(Cost.Cost(bone_amount,Items.Bone))
	main()	