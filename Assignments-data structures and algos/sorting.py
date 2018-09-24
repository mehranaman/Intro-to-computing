#  File: sorting.py
#  Description: Sorting algorithms
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: Nov 26, 2017
#  Date Last Modified: Dec 1st, 2017

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

################################################################

#helper function for generating random lists   
def random_helper(n):
    random_list = []
    for i in range(n):
        temp = random.randint(1,9999)
        random_list.append(temp)
        
    return random_list


#sorting random lists function for all algorithms
def sort_random():


    #first we tackle bubble sort
    
    bubble_time = []

    for i in range(5):
        random_list = random_helper(10)
        
        start_time = time.time()
        bubbleSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)

    

    average_bubble_10 = (sum(bubble_time))/5

    bubble_time = []
    
    for i in range (5):
        random_list = random_helper(100)
        start_time = time.time()
        bubbleSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
    average_bubble_100 = (sum(bubble_time))/100


    bubble_time = []
    
    for i in range (5):
        random_list = random_helper(1000)
        start_time = time.time()
        bubbleSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
        
    average_bubble_1000 = (sum(bubble_time))/1000

    
        

    #Next is insertion sort

    insertion_time = []

    for i in range(5):
        random_list = random_helper(10)
        start_time = time.time()
        insertionSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
    

    average_insertion_10 = (sum(insertion_time))/5

    insertion_time = []
    
    for i in range (5):
        random_list = random_helper(100)
        start_time = time.time()
        insertionSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
    average_insertion_100 = (sum(insertion_time))/100


    insertion_time = []
    
    for i in range (5):
        random_list = random_helper(1000)
        start_time = time.time()
        insertionSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
        
    average_insertion_1000 = (sum(insertion_time))/1000


    #next merge sort

    merge_time = []
    
    for i in range(5):
        random_list = random_helper(10)
        start_time = time.time()
        mergeSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)


    average_merge_10 = (sum(merge_time))/5

    merge_time = []
    
    for i in range (5):
        random_list = random_helper(100)
        start_time = time.time()
        mergeSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_100 = (sum(merge_time))/100


    insertion_time = []
    
    for i in range (5):
        random_list = random_helper(1000)
        start_time = time.time()
        mergeSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_1000 = (sum(merge_time))/1000
    

    
    #lastly quick sort

    quick_time = []

    for i in range(5):
        random_list = random_helper(10)
        start_time = time.time()
        quickSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)


    average_quick_10 = (sum(quick_time))/5

    quick_time = []
    
    for i in range (5):
        random_list = random_helper(100)
        start_time = time.time()
        quickSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
    average_quick_100 = (sum(quick_time))/100


    quick_time = []
    
    for i in range (5):
        random_list = random_helper(1000)
        start_time = time.time()
        quickSort(random_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
        
    average_quick_1000 = (sum(quick_time))/1000
    

    print()
    print("Input type = Random")
    print(format('',"26s"), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'))


    print(format("   Sort function", "26s"), end = '')
    print(format("   (n=10)", "26s"), end = '')
    print(format("   (n=100)","26s"), end = '')
    print(format("   (n=1000)", "26s"))

    print('------------------------------------------------------------------------------------------------')


    average_bubble_10 = '{:06.6f}'.format(average_bubble_10)
    average_bubble_100 = '{:06.6f}'.format(average_bubble_100)
    average_bubble_1000 = '{:06.6f}'.format(average_bubble_1000)
    
    print(format("   bubble sort", "26s"), end = '')
    print(format("   " + str(average_bubble_10), "26s"), end = '')
    print(format("   " + str(average_bubble_100), "26s"), end = '')
    print(format("   "+ str(average_bubble_1000), "26s"))
    
    average_insertion_10 = '{:06.6f}'.format(average_insertion_10)
    average_insertion_100 = '{:06.6f}'.format(average_insertion_100)
    average_insertion_1000 = '{:06.6f}'.format(average_insertion_1000)
    

    print(format("   insertion sort", "26s"), end = '')
    print(format("   " + str(average_insertion_10), "26s"), end = '')
    print(format("   "+str(average_insertion_100), "26s"), end = '')
    print(format("   "+ str(average_insertion_1000), "26s"))
    
    average_merge_10 = '{:06.6f}'.format(average_merge_10)
    average_merge_100 = '{:06.6f}'.format(average_merge_100)
    average_merge_1000 = '{:06.6f}'.format(average_merge_1000)

    print(format("   merge sort", "26s"), end = '')
    print(format("   "+ str(average_merge_10), "26s"), end = '')
    print(format("   " + str(average_merge_100), "26s"), end = '')
    print(format("   "+ str(average_merge_1000), "26s"))

    average_quick_10 = '{:06.6f}'.format(average_quick_10)
    average_quick_100 = '{:06.6f}'.format(average_quick_100)
    average_quick_1000 = '{:06.6f}'.format(average_quick_1000)

    print(format("   quick sort", "26s"), end = '')
    print(format("   "+ str(average_quick_10), "26s"), end = '')
    print(format("   "+ str(average_quick_100), "26s"), end = '')
    print(format("   "+ str(average_quick_1000), "26s"), end = '')
    print()
    


def sorted_helper(n):
    
    sorted_list = []
    for i in range(n):
        #keeping it i+1 to keep all values positive
        temp = i+1
        sorted_list.append(temp)
        
    return sorted_list


def sort_sorted():
    bubble_time = []

    for i in range(5):
        
        sorted_list = sorted_helper(10)
        start_time = time.time()
        bubbleSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
    

    average_bubble_10 = (sum(bubble_time))/5
    
    bubble_time = []
    
    for i in range (5):
        sorted_list = sorted_helper(100)
        start_time = time.time()
        bubbleSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
    average_bubble_100 = (sum(bubble_time))/100


    bubble_time = []
    
    for i in range (5):
        
        sorted_list = sorted_helper(1000)
        start_time = time.time()
        bubbleSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
        
    average_bubble_1000 = (sum(bubble_time))/1000

    
        

    #Next is insertion sort
    
    insertion_time = []

    for i in range(5):
        
        sorted_list = sorted_helper(10)
        start_time = time.time()
        insertionSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)


    average_insertion_10 = (sum(insertion_time))/5

    
    insertion_time = []
    
    for i in range (5):
        sorted_list = sorted_helper(100)
        start_time = time.time()
        insertionSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
        
    average_insertion_100 = (sum(insertion_time))/100


    insertion_time = []
    
    for i in range (5):
        sorted_list = sorted_helper(1000)
        start_time = time.time()
        insertionSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
        
    average_insertion_1000 = (sum(insertion_time))/1000


    #next merge sort

    merge_time = []

    for i in range(5):
        sorted_list = sorted_helper(10)
        start_time = time.time()
        mergeSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)


    average_merge_10 = (sum(merge_time))/5

    merge_time = []
    
    for i in range (5):
        sorted_list = sorted_helper(100)
        start_time = time.time()
        mergeSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_100 = (sum(merge_time))/100



    insertion_time = []
    
    for i in range (5):
        sorted_list = sorted_helper(1000)
        start_time = time.time()
        mergeSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_1000 = (sum(merge_time))/1000
    
    
        
    #lastly quick sort

    quick_time = []

    for i in range(5):
        sorted_list = sorted_helper(10)
        start_time = time.time()
        quickSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)

    
    average_quick_10 = (sum(quick_time))/5
    
    quick_time = []
    
    for i in range (5):
        sorted_list = sorted_helper(100)
        start_time = time.time()
        quickSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
    average_quick_100 = (sum(quick_time))/100


    quick_time = []
    
    for i in range (5):
        sorted_list = sorted_helper(1000)
        start_time = time.time()
        quickSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
        
    average_quick_1000 = (sum(quick_time))/1000

    print()
    print("Input type = Sorted")
    print(format('',"26s"), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'))


    print(format("   Sort function", "26s"), end = '')
    print(format("   (n=10)", "26s"), end = '')
    print(format("   (n=100)","26s"), end = '')
    print(format("   (n=1000)", "26s"))

    print('------------------------------------------------------------------------------------------------')


    average_bubble_10 = '{:06.6f}'.format(average_bubble_10)
    average_bubble_100 = '{:06.6f}'.format(average_bubble_100)
    average_bubble_1000 = '{:06.6f}'.format(average_bubble_1000)
    
    print(format("   bubble sort", "26s"), end = '')
    print(format("   " + str(average_bubble_10), "26s"), end = '')
    print(format("   " + str(average_bubble_100), "26s"), end = '')
    print(format("   "+ str(average_bubble_1000), "26s"))
    
    average_insertion_10 = '{:06.6f}'.format(average_insertion_10)
    average_insertion_100 = '{:06.6f}'.format(average_insertion_100)
    average_insertion_1000 = '{:06.6f}'.format(average_insertion_1000)
    

    print(format("   insertion sort", "26s"), end = '')
    print(format("   " + str(average_insertion_10), "26s"), end = '')
    print(format("   "+str(average_insertion_100), "26s"), end = '')
    print(format("   "+ str(average_insertion_1000), "26s"))
    
    average_merge_10 = '{:06.6f}'.format(average_merge_10)
    average_merge_100 = '{:06.6f}'.format(average_merge_100)
    average_merge_1000 = '{:06.6f}'.format(average_merge_1000)

    print(format("   merge sort", "26s"), end = '')
    print(format("   "+ str(average_merge_10), "26s"), end = '')
    print(format("   " + str(average_merge_100), "26s"), end = '')
    print(format("   "+ str(average_merge_1000), "26s"))

    average_quick_10 = '{:06.6f}'.format(average_quick_10)
    average_quick_100 = '{:06.6f}'.format(average_quick_100)
    average_quick_1000 = '{:06.6f}'.format(average_quick_1000)

    print(format("   quick sort", "26s"), end = '')
    print(format("   "+ str(average_quick_10), "26s"), end = '')
    print(format("   "+ str(average_quick_100), "26s"), end = '')
    print(format("   "+ str(average_quick_1000), "26s"), end = '')
    print()

def reverse_helper(n):
    
    reverse_list = []
    for i in range(n):
        temp = n-i
        reverse_list.append(temp)
        
    return reverse_list



def sort_reverse():
    bubble_time = []

    for i in range(5):
        reverse_list = reverse_helper(10)
        start_time = time.time()
        bubbleSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)


    average_bubble_10 = (sum(bubble_time))/5

    bubble_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(100)
        start_time = time.time()
        bubbleSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
    average_bubble_100 = (sum(bubble_time))/100


    bubble_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(1000)
        start_time = time.time()
        bubbleSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
        
    average_bubble_1000 = (sum(bubble_time))/1000

    
        

    #Next is insertion sort

    insertion_time = []

    for i in range(5):
        reverse_list = reverse_helper(10)
        start_time = time.time()
        insertionSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)


    average_insertion_10 = (sum(insertion_time))/5

    insertion_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(100)
        start_time = time.time()
        insertionSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
        
    average_insertion_100 = (sum(insertion_time))/100


    insertion_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(1000)
        start_time = time.time()
        insertionSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
        
    average_insertion_1000 = (sum(insertion_time))/1000


    #next merge sort

    merge_time = []

    for i in range(5):
        reverse_list = reverse_helper(10)
        start_time = time.time()
        mergeSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)


    average_merge_10 = (sum(merge_time))/5

    merge_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(100)
        start_time = time.time()
        mergeSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_100 = (sum(merge_time))/100


    insertion_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(1000)
        start_time = time.time()
        mergeSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_1000 = (sum(merge_time))/1000
    

    
    #lastly quick sort

    quick_time = []

    for i in range(5):
        reverse_list = reverse_helper(10)
        start_time = time.time()
        quickSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)


    average_quick_10 = (sum(quick_time))/5

    quick_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(100)
        start_time = time.time()
        quickSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
    average_quick_100 = (sum(quick_time))/100


    quick_time = []
    
    for i in range (5):
        reverse_list = reverse_helper(1000)
        start_time = time.time()
        quickSort(reverse_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
        
    average_quick_1000 = (sum(quick_time))/1000

    print()
    print("Input type = Reverse")
    print(format('',"26s"), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'))


    print(format("   Sort function", "26s"), end = '')
    print(format("   (n=10)", "26s"), end = '')
    print(format("   (n=100)","26s"), end = '')
    print(format("   (n=1000)", "26s"))

    print('------------------------------------------------------------------------------------------------')


    average_bubble_10 = '{:06.6f}'.format(average_bubble_10)
    average_bubble_100 = '{:06.6f}'.format(average_bubble_100)
    average_bubble_1000 = '{:06.6f}'.format(average_bubble_1000)
    
    print(format("   bubble sort", "26s"), end = '')
    print(format("   " + str(average_bubble_10), "26s"), end = '')
    print(format("   " + str(average_bubble_100), "26s"), end = '')
    print(format("   "+ str(average_bubble_1000), "26s"))
    
    average_insertion_10 = '{:06.6f}'.format(average_insertion_10)
    average_insertion_100 = '{:06.6f}'.format(average_insertion_100)
    average_insertion_1000 = '{:06.6f}'.format(average_insertion_1000)
    

    print(format("   insertion sort", "26s"), end = '')
    print(format("   " + str(average_insertion_10), "26s"), end = '')
    print(format("   "+str(average_insertion_100), "26s"), end = '')
    print(format("   "+ str(average_insertion_1000), "26s"))
    
    average_merge_10 = '{:06.6f}'.format(average_merge_10)
    average_merge_100 = '{:06.6f}'.format(average_merge_100)
    average_merge_1000 = '{:06.6f}'.format(average_merge_1000)

    print(format("   merge sort", "26s"), end = '')
    print(format("   "+ str(average_merge_10), "26s"), end = '')
    print(format("   " + str(average_merge_100), "26s"), end = '')
    print(format("   "+ str(average_merge_1000), "26s"))

    average_quick_10 = '{:06.6f}'.format(average_quick_10)
    average_quick_100 = '{:06.6f}'.format(average_quick_100)
    average_quick_1000 = '{:06.6f}'.format(average_quick_1000)

    print(format("   quick sort", "26s"), end = '')
    print(format("   "+ str(average_quick_10), "26s"), end = '')
    print(format("   "+ str(average_quick_100), "26s"), end = '')
    print(format("   "+ str(average_quick_1000), "26s"), end = '')
    print()

    
def almost_sorted_helper(n):
    sorted_list = []
    for i in range(n):
        temp = i+1
        sorted_list.append(temp)

    for i in range (n//10):
        p = random.randint(0,n-1)
        q = p
        while p == q:
            q = random.randint(0,n-1)
        
        sorted_list[q],sorted_list[p] = sorted_list[p],sorted_list[q]

    return sorted_list

def sort_almostSorted():
    bubble_time = []

    for i in range(5):
        sorted_list = almost_sorted_helper(10)
        start_time = time.time()
        bubbleSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)


    average_bubble_10 = (sum(bubble_time))/5

    bubble_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(100)
        start_time = time.time()
        bubbleSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
    average_bubble_100 = (sum(bubble_time))/100


    bubble_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(1000)
        start_time = time.time()
        bubbleSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        bubble_time.append(duration)
        
    average_bubble_1000 = (sum(bubble_time))/1000

    
        

    #Next is insertion sort

    insertion_time = []

    for i in range(5):
        sorted_list = almost_sorted_helper(10)
        start_time = time.time()
        insertionSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)


    average_insertion_10 = (sum(insertion_time))/5

    insertion_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(100)
        start_time = time.time()
        insertionSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
        
    average_insertion_100 = (sum(insertion_time))/100


    insertion_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(1000)
        start_time = time.time()
        insertionSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        insertion_time.append(duration)
        
    average_insertion_1000 = (sum(insertion_time))/1000


    #next merge sort

    merge_time = []

    for i in range(5):
        sorted_list = almost_sorted_helper(10)
        start_time = time.time()
        mergeSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)


    average_merge_10 = (sum(merge_time))/5

    merge_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(100)
        start_time = time.time()
        mergeSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_100 = (sum(merge_time))/100


    insertion_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(1000)
        start_time = time.time()
        mergeSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        merge_time.append(duration)
        
    average_merge_1000 = (sum(merge_time))/1000
    

    
    #lastly quick sort

    quick_time = []

    for i in range(5):
        sorted_list = almost_sorted_helper(10)
        start_time = time.time()
        quickSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)


    average_quick_10 = (sum(quick_time))/5

    quick_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(100)
        start_time = time.time()
        quickSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
    average_quick_100 = (sum(quick_time))/100


    quick_time = []
    
    for i in range (5):
        sorted_list = almost_sorted_helper(1000)
        start_time = time.time()
        quickSort(sorted_list)
        end_time = time.time()
        duration = end_time - start_time
        quick_time.append(duration)
        
    average_quick_1000 = (sum(quick_time))/1000
    
    print()
    print("Input type = Almost sorted")
    print(format('',"26s"), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'), end = '')
    print(format("   avg time", '26s'))


    print(format("   Sort function", "26s"), end = '')
    print(format("   (n=10)", "26s"), end = '')
    print(format("   (n=100)","26s"), end = '')
    print(format("   (n=1000)", "26s"))

    print('------------------------------------------------------------------------------------------------')


    average_bubble_10 = '{:06.6f}'.format(average_bubble_10)
    average_bubble_100 = '{:06.6f}'.format(average_bubble_100)
    average_bubble_1000 = '{:06.6f}'.format(average_bubble_1000)
    
    print(format("   bubble sort", "26s"), end = '')
    print(format("   " + str(average_bubble_10), "26s"), end = '')
    print(format("   " + str(average_bubble_100), "26s"), end = '')
    print(format("   "+ str(average_bubble_1000), "26s"))
    
    average_insertion_10 = '{:06.6f}'.format(average_insertion_10)
    average_insertion_100 = '{:06.6f}'.format(average_insertion_100)
    average_insertion_1000 = '{:06.6f}'.format(average_insertion_1000)
    

    print(format("   insertion sort", "26s"), end = '')
    print(format("   " + str(average_insertion_10), "26s"), end = '')
    print(format("   "+str(average_insertion_100), "26s"), end = '')
    print(format("   "+ str(average_insertion_1000), "26s"))
    
    average_merge_10 = '{:06.6f}'.format(average_merge_10)
    average_merge_100 = '{:06.6f}'.format(average_merge_100)
    average_merge_1000 = '{:06.6f}'.format(average_merge_1000)

    print(format("   merge sort", "26s"), end = '')
    print(format("   "+ str(average_merge_10), "26s"), end = '')
    print(format("   " + str(average_merge_100), "26s"), end = '')
    print(format("   "+ str(average_merge_1000), "26s"))

    average_quick_10 = '{:06.6f}'.format(average_quick_10)
    average_quick_100 = '{:06.6f}'.format(average_quick_100)
    average_quick_1000 = '{:06.6f}'.format(average_quick_1000)

    print(format("   quick sort", "26s"), end = '')
    print(format("   "+ str(average_quick_10), "26s"), end = '')
    print(format("   "+ str(average_quick_100), "26s"), end = '')
    print(format("   "+ str(average_quick_1000), "26s"), end = '')
    print()    





def main():

    
    sort_random()
    sort_sorted()
    sort_reverse()
    sort_almostSorted()

main()

    
       
    
    

        
    
    

    



