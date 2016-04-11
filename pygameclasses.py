from random import randint
class Adventurer():
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
		self.health = 120
		if self.strength < 5:
			self.strength = 5
		self.speed += 1
		if self.intelligence > 2:
			self.intelligence -= 2
		if self.toughness < 5:
			self.toughness += 3
		elif self.toughness > 5:
			self.toughness += 1