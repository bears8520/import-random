import random

r = random.randint(1, 100)
count = 0

while True:
	n = int(input('猜一數字: '))
	if n == r:
		print('你猜對了')
		break
	elif n < r:
		print('要再大')
	elif n > r:
		print('要再小')