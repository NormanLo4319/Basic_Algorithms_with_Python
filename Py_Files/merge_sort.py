# Merge Sort Algorithm

# Create three lists
list1 = [20, 45, 51, 88, 99999]
list2 = [98, 10, 23, 15, 99999]
list3 = []

# Define merge_sort function
def merge_sort():
    global list1
    global list2
    global list3
    
    # First sort list 1 and 2, then merge the two
    select_sort(list1, len(list1)-1)
    select_sort(list2, len(list2)-1)
    
    print('\n List 1 Sorted Result: ', end='')
    for i in range(len(list1)-1):
        print(list1[i], '', end='')
    
    print('\n List 2 Sorted Result: ', end='')
    for i in range(len(list2)-1):
        print(list2[i], '', end='')
    print()
    
    for i in range(60):
        print('=', end='')
    print()
    
    my_merge(len(list1)-1, len(list2)-1)
    
    for i in range(60):
        print('=', end='')
    print()
    
    print('\n Merged Sorting Result: ', end='')
    for i in range(len(list1)+len(list2)-2):
        print('%d ' % list3[i], end='')

# Define select_sort function
def select_sort(data, size):
    for base in range(size-1):
        small = base
        for j in range(base+1, size):
            if data[j] < data[small]:
                small = j
        data[small], data[base] = data[base], data[small]

# Define my_merge function
def my_merge(size1, size2):
    global list1
    global list2
    global list3
    
    index1 = 0
    index2 = 0
    for index3 in range(len(list1)+len(list2)-2):
        if list1[index1] < list2[index2]:
            list3. append(list1[index1])
            index1 += 1
            print('This number %d is coming from list 1 ' % list3[index3])
        else:
            list3.append(list2[index2])
            index2 += 1
            print('This number %d is coming from list 2 ' % list3[index3])
        print('The current ordering is: ', end='')
        for i in range(index3+1):
            print(list3[i], ' ', end='')
        print('\n')

merge_sort()