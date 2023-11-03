""" write a program to find prime upto given range number """

number_range= int(input('Enter range to get prime numbers: '))

nums = []

for i in range(2, number_range):
    flag = True
    for j in range(2,i):
        if (i%j == 0):
            flag = False
            break

        else:
            flag  = True
    if flag:
        nums.append(i)


print(nums)


