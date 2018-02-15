'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


num = 2520  # I am starting from 2520 because it was the case for 1 to 10

while True:
	if (num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and 
	num % 11 == 0 and num % 13 == 0 and num % 16 == 0 and num % 17 == 0 and num % 19 == 0):
		break  # I got that smallest number so breaking the infinite loop
	num += 1

print 'Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is', num

# Answer = 232792560