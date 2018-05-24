import random
list_of_entries = ('Mickey', 'Minnie', 'Donald', 'Daisy', 'Goofy', 'Pluto')
list_of_winners = []

while len(list_of_winners) < 3:
	winner = []
	winner = random.choice(list_of_entries)
	list_of_winners.append(winner)
	
print(list_of_winners)
