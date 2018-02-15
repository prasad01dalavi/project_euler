''' The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 285 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

sum_of_square = 0
sum = 0
square_of_sum = 0

for number in range(1, 101):
    sum_of_square += number*number

for number in range(1, 101):
    sum += number
square_of_sum = sum*sum

difference = square_of_sum - sum_of_square
print 'Difference = ', difference

# Answer = 25164150
