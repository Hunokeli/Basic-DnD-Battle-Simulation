import random

class Character:

	def __init__(self, name, ac, hp, dmg, bonus):
		self.name = name
		self.ac = ac
		self.hp = hp
		self.dmg = dmg
		self.b = bonus
	
	def __str__(self):
		return f'Name: {self.name}\nAC: {self.ac}\nHP: {self.hp}\nDMG: {self.dmg} DMG\nAttack Bonus: +{self.b}'

#PARTY
pumpeck = Character('Pumpeck', 15, 50, 5, 5)
rum = Character('Rum', 15, 50, 5, 5)
thor = Character('Thorfreyer', 15, 50, 5, 5)
niama = Character('Niama', 15, 50, 5, 5)
vel = Character('Veldora', 15, 50, 5, 5)

#MONSTERS
goblin1 = Character('Goblin one', 15, 50, 5, 5)
goblin2 = Character('Goblin two', 15, 50, 5, 5)

wins = 0
runs = 1000

for i in range(runs):

	party = [thor,pumpeck]
	enemies = [goblin1,goblin2]
	php=[]
	ehp = []
	for e in range(len(enemies)):
		ehp.append(enemies[e].hp)

	for p in range(len(party)):
		php.append(party[p].hp)



	while len(party) > 0 and len(enemies) > 0:

		for a in range(len(party)):
			etarget = random.choice(enemies)
			if random.randint(1,20) + party[a].b >= etarget.ac:
				ehp[enemies.index(etarget)] -= party[a].dmg
				if ehp[enemies.index(etarget)] <= 0:
					ehp.pop(enemies.index(etarget))
					enemies.remove(etarget)
				if len(enemies)==0:
					wins+=1
					break

		for e in range(len(enemies)):
			ptarget = random.choice(party)
			if random.randint(1,20) + enemies[e].b >= ptarget.ac:
				php[party.index(ptarget)] -= enemies[e].dmg
				if php[party.index(ptarget)] <= 0:
					php.pop(party.index(ptarget))
					party.remove(ptarget)
				if len(party)==0:
					break

total = (wins/runs)*100
print(f'won {total}% of the time')
