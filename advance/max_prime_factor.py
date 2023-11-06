""" implement a function that takes a natural number as an argument and returns the greatest prime factor of that number. """

num = int(input("Enter a number to get its prime factor: "))

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    return True

def factor(num):
    lst = []
    for i in range(2,num):
        if num%i == 0:
            lst.append(i)
    lst = lst[::-1]
    for numbers in lst:
        if isPrime(numbers):
            return numbers


# prime_factors = factor(num)

# for number in prime_factors:
#     if isPrime(number):
#         print(f'greates prime factor of {num} is: {number}')
#         break

print(factor(num))