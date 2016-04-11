from random import randint
class Adventurer():
	# This is the default job class
	def __init__(self, name, job="Adventurer"):
		self.name = name
		self.job = job
		self.health = 100
		self.strength = randint(1, 10)
		self.intelligence = randint(1, 10)
		self.speed = randint(1, 10)
		self.toughness = randint(1, 10)

	def __str__(self):
		return "{} is a(n) {} with {} strength, {} intelligence, {} speed, and {} toughness.".format(self.name, self.job, self.strength, self.intelligence, self.speed, self.toughness)

# Warrior Job
class Warrior(Adventurer):
	def __init__(self, name):
		super().__init__(name, job="Warrior")
		# Health is set to 120
		self.health = 120
		# Strength must be at least 5 for a warrior and if initial roll
		# is over 5 then strength increases by 1
		if self.strength < 5:
			self.strength = 5
		elif self.strength > 5:
			self.strength += 1;
		# Speed and intelligence roll within a different range than the default job class
		self.speed = randint(3, 8);
		self.intelligence = randint(2, 8);
		# Similar to strength, warrior's toughness cannot be less than 5
		if self.toughness < 5:
			self.toughness = 5
		elif self.toughness > 5:
			self.toughness += 1

	def savage_roar(self):
		print("The warrior yells out in anger! Overwhelming fury increases the warrior's strength.")
		self.strength += 1
		if self.intelligence > 2:
			self.intelligence -= 1
		self.health -= 10

# Thief Job
class Thief(Adventurer):
	def __init__(self, name):
		super().__init__(name, job="Thief")
		# All new ranges for strength, speed, and intelligence
		# Toughness rolls are left at default
		self.strength = randint(2, 6)
		self.speed = randint(5, 11)
		self.intelligence = randint(5, 11)

	def steal(self):
		print("The thief uses 'steal'!")