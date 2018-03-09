# Imagine your friend bets he can beat you in a game of dice.
# He says you'll both roll one dice each, and if the highest number that gets rolled is a 5 or a 6, he wins. 
# If the highest number you both roll is below a 5, then you win.
# Should you take the bet? What are the odds you would win if you played this game 100,000 times?
from random import randint
def experiment(n):
	count = 0
	p1 = 0
	p2 = 0
	while count < n:       
		d1=randint(2,14)
		d2=randint(2,14)
		if d1>=11 or d2>=11:
			p2 = p2 + 1
			count = count + 1
		else:	
			p1 = p1 + 1
			count = count + 1
	print("Player 1 wins: ", p1)
	print("Player 2 wins: ", p2)
	print("Total Games Played: ", p1 + p2)
	
experiment(1000)

	
