import random
r = random.randint(1, 100)
while True:
	number = input('Please guess a number from 1 to 100:')
	number = int(number)
	if number == r:
		print('Congratulation!You are right!')
		break
	elif number < r:
		print('Wrong! The number is bigger.')
	else: 
		print('Wrong! The number is smaller')