# Binary Search Algorithm

# Importing dependency
import random

# Define bin_search function
def bin_search(data, val):
    low = 0
    high = 49
    while low <= high and val !=-1:
        mid=int((low+high)/2)
        if val<data[mid]:
            print('%d Between values %d[%3d] and the middle value %d[%3d], Search half on the left' \
                 %(val, low+1, data[low], mid+1, data[mid]))
            high = mid-1
        elif val>data[mid]:
            print('%d Between the middle values %d[%3d] and %d[%3d], Search half on the right' \
                 %(val, mid+1, data[mid], high+1, data[high]))
            low=mid+1
        else:
            return mid
    return -1

# Create the testing values
val = 1
data = [0]*50
for i in range(50):
    data[i]=val
    val=val+random.randint(1, 5)

# Create a custom input for binary search
while True:
    num=0
    val=int(input('Enter a search key (1 - 150), enter -1 to end: '))
    if val == -1:
        break
    num=bin_search(data,val)
    if num == -1:
        print('##### Cannot Find [%3d] #####' %val)
    else:
        print('We found [%3d] at position %2d' %(data[num], num+1))

print('Data Information')
for i in range(5):
    for j in range(10):
        print('%3d-%-3d' %(i*10+j+1, data[i*10+j]), end='')
    print()