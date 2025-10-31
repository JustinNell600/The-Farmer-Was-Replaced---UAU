def Changehat():
	Hatlist = [
	Hats.Brown_Hat,
	Hats.Cactus_Hat,
	Hats.Carrot_Hat,
	Hats.Gold_Hat,
	Hats.Gray_Hat,
	Hats.Green_Hat,
	Hats.Purple_Hat,
	Hats.Straw_Hat,
	Hats.Traffic_Cone,
	Hats.Tree_Hat,
	Hats.Wizard_Hat,
	Hats.Pumpkin_Hat]
	
	index = random() * len(Hatlist) // 1
	
	change_hat(Hatlist[index])