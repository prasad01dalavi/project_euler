'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        product = str(num1*num2)
        if num1*num2 == 906609:
            print 'yes', num1, num2
        if product == product[::-1]:
            palindromic = product

print 'Palindromatic Number =', palindromic
