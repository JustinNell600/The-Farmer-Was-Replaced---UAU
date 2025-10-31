def Water():
	if get_water() < 1 and num_items(Items.Water) >= get_world_size() ** 2:
		use_item(Items.Water)
		