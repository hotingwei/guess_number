import random
start = input('Please choose the start of the guessing range:')
end = input('Please choose the end of the guessing range:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	number = input('Please guess a number:')
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