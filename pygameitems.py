class Item():
	# This is the base class for all items
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
	def __str__(self):
		return "[{}]\n------\nDescription: {}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
	# This class defines the base currency and inherits from Item
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Gold", description="A round gold coin with {} stamped on the front.".format(str(self.amt)), value=self.amt)

class Weapon(Item):
	# This class is the parent class for all weapons and inherits from Item
	def __init__(self, name, description, value, damage, special):
		self.damage = damage
		self.special = special
		super().__init__(name, description, value)
	def __str__(self):
		return "[{}]\n------\nDescription: {}\nValue: {}\nDamage: [{}]\nSpecial: {}".format(self.name, self.description, self.value, self.damage, self.special)

class Dagger(Weapon):
	def __init__(self, name, description, value, damage, special):
		super().__init__(name, description, value, damage, special);

class Sword(Weapon):
	def __init__(self, name, description, value, damage, special):
		super().__init__(name, description, value, damage, special);

class Bow(Weapon):
	def __init__(self, name, description, value, damage, special):
		super().__init__(name, description, value, damage, special);

# Dagger Weapons
rusted_dagger = Dagger("Rusted Dagger", "A significantly rusted dagger, it's still somewhat usable as a weapon.", 0, 5, "Poison")
shiny_dagger = Dagger("Shiny Dagger", "A very shiny dagger.", 5, 10, "None")
serrated_dagger = Dagger("Serrated Dagger", "A dagger with teeth, this could cause some serious damage.", 10, 15, "Bleed")
swordbreaker = Dagger("Swordbreaker", "A dagger of this quality can certainly break some poor quality swords.", 30, 25, "None")
resentment = Dagger("Resentment", "A resentful spirit lives within this dagger.", 55, 40, "Curse")
meteor = Dagger("Meteor", "Blessed with an enchantment, this dagger increases the speed of its wielder.", 100, 35, "Speed+")

# Sword Weapons
broken_sword = Sword("Broken Sword", "The broken sword of a long dead knight. It's still quite sharp.", 1, 10, "None")
shiny_sword = Sword("Shiny Sword", "A very shiny sword.", 10, 15, "None")
claymore = Sword("Claymore", "A 2-handed sword, its weight is almost as deadly as its edge.", 20, 25, "Range+")
great_sword = Sword("Great Sword", "A 2-handed sword with a very keen edge.", 30, 35, "Range+")
dark_blade = Sword("Dark Blade", "Spirits of darkness are drawn to this cursed sword.", 45, 45, "Curse")
excalibur = Sword("Excalibur", "A legendary sword that actually lives up to its name.", 100, 45, "Inspire")

# Bow Weapons
old_bow = Bow("Old Bow", "An old bow.", 1, 5, "Far Range")
decent_bow = Bow("Decent Bow", "A decent bow.", 5, 10, "Far Range")
better_bow = Bow("Better Bow", "A bow that's actually pretty good.", 10, 15, "Far Range")
great_bow = Bow("Great Bow", "A bow with incredibly deadly range.", 15, 25, "Far Range+")
eagle_eye = Bow("Eagle Eye", "A bow that gives its wielder the accuracy of an eagle.", 20, 35, "Far Range++")
falling_star = Bow("Falling Star", "This bow was forged from a fallen star and gives its wielder godlike accuracy.", 35, 45, "Godsight")