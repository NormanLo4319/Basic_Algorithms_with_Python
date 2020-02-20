# Tower of Hanoi Algorithm

# Define hanoi function
def hanoi(n, p1, p2, p3):
    if n == 1:
        print('Disk is moving from %d to %d' %(p1, p3))
    else:
        hanoi(n-1, p1, p3, p2)
        print('Disk is moving from %d to %d' %(p1, p3))
        hanoi(n-1, p2, p1, p3)

# Create input statement
j = int(input('Enter the total number of disk: '))
hanoi(j, 1, 2, 3)