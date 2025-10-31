def Fertilizer():
	if num_items(Items.Fertilizer) >= num_drones():
		use_item(Items.Fertilizer)
	else:
		pass