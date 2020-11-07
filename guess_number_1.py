import random
r = random.randint(1, 100)
count = 0
while True:
	number = input('Please guess a number from 1 to 100:')
	number = int(number)
	count = count + 1
	if number == r:
		print('Congratulation!You are right!')
		print('you have guessed', count, 'times')
		break
	elif number < r:
		print('Wrong! The number is bigger.')
	else: 
		print('Wrong! The number is smaller')
	print('you have guessed', count, 'times')