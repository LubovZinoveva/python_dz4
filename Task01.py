# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factorization(number):
    result = []
    for i in range(2, int((number)**0.5+1)):
        while number % i == 0:
            result.append(i)
            number //= i
    if (number != 1): 
        result.append(number)
    return result

n = int(input('N = '))
factors = prime_factorization(n)
print(factors)