'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

factor_list = []
target = 1
factor = 2


def prime_check(number):
    prime_flag = 0
    for divisor in range(2, number/2 + 1):
        if number % divisor == 0:
            prime_flag = False
            break
        else:
            prime_flag = True
    return prime_flag



while True:
    if prime_check(factor) and 600851475143 % factor == 0:
        target = target * factor
        factor_list.append(factor)
        if target == 600851475143:
            break
    factor += 1


print 'Prime Factor List =', factor_list

# Answer = 6857
