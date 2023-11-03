"""write a program to bubble short a given list"""

lst = input('enter number seperated with comma: ')

lst = lst.split(',')
lst = list(map(int, lst))
print(f'list befor sorting: {lst}')

n = len(lst)

for i in range(n):
    for j in range(n-1):
        if lst[j] > lst[i]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(f'list after sorting: {lst}')