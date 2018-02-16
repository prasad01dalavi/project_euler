'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

cnt = 0
num = 1


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
    if prime_check(num):
        cnt += 1

    if cnt == 9999:          # Excluding 2 and 3 prime numbers so subtracting 2 from required count
        print num
        break

    num += 1

# Answer = 104743
