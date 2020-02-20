# Quicksort Algorithm

# Import dependency
import random

# Define inputarr function
def inputarr(data, size):
    for i in range(size):
        data[i]=random.randint(1, 100)

# Define showdata function
def showdata(data, size):
    for i in range(size):
        print('%3d' %data[i], end='')

# Define quick function
def quick(d, size, lf, rg):
    if lf < rg:
        lf_idx=lf+1
        while d[lf_idx] < d[lf]:
            if lf_idx+1 > size:
                break
            lf_idx += 1
        rg_idx=rg
        while d[rg_idx] > d[lf]:
            rg_idx -= 1
        while lf_idx < rg_idx:
            d[lf_idx], d[rg_idx] = d[rg_idx], d[lf_idx]
            lf_idx += 1
            while d[lf_idx] < d[lf]:
                lf_idx += 1
            rg_idx -= 1
            while d[rg_idx] > d[lf]:
                rg_idx -= 1
        d[lf], d[rg_idx] = d[rg_idx], d[lf]
        
        for i in range(size):
            print('%3d' %d[i], end='')
        print()
        
        quick(d, size, lf, rg_idx-1)
        quick(d, size, rg_idx+1, rg)

# Define main function
def main():
    data=[0]*100
    size=int(input('Enter the size of the array for sorting (less than 100): '))
    inputarr(data, size)
    print('------------------------------------------')
    print('Random Generated Data Output: ')
    showdata(data,size)
    print('\n')
    print('------------------------------------------')
    print('Sorting Process: ')
    quick(data,size,0,size-1)
    print('------------------------------------------')
    print('Quicksort Result: ')
    showdata(data,size)
main()