CItem =[
Items.Carrot,
Items.Pumpkin,
Items.Cactus,
Items.Bone]

def ceil(x):
	return -((-x) // 1)
	
def Cost(Needed,Current_item):
	NeededCost=Needed-num_items(Current_item)
	if Current_item == Items.Carrot:
		per = (1*(2**(num_unlocked(Unlocks.Carrots)-1)))
		field = per * (get_world_size()**2)//2
		Plants = get_world_size()**2
		return (Plants*2**(num_unlocked(Unlocks.Carrots)-1))*ceil(NeededCost/field)
	if Current_item == Items.Pumpkin:
		field = (get_world_size()**2*6)*(2**(num_unlocked(Unlocks.Pumpkins)-1))//2
		Plants = (get_world_size()**2)+ceil((0.20*(get_world_size()**2)))
		return (Plants*2**(num_unlocked(Unlocks.Pumpkins)-1))*ceil((NeededCost/field))
	if Current_item == Items.Cactus:
		field = ((get_world_size()**2)**2)*2**(num_unlocked(Unlocks.Cactus))
		Plants= (get_world_size()**2)
		return (Plants*2**(num_unlocked(Unlocks.Cactus)))*ceil(NeededCost/field)
	if Current_item == Items.Bone:
		field = (((get_world_size()**2)-1)**2)*2**(num_unlocked(Unlocks.Dinosaurs))
		Plants= (get_world_size()**2)
		return (Plants*2**(num_unlocked(Unlocks.Dinosaurs)))*ceil(NeededCost/field)
		
	
		
	
	