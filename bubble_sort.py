#Bubble Sort is a sorting technique which iterates over the list repeatly 
#and compares each element with adjacent element and swaps them if there are in wrong order
#this will continue untill all elements are in sorted order

def bubble_sort(num):
    for i in range(len(num)):
        for j in range(0,len(num)-i-1):
            if(num[j]>num[j+1]):
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp


num = [1,6,9,56,2,76,0]
bubble_sort(num)
print(num)

"""
Bubble sort has a time complexity of O(n^2) because it involves nested loops where the number of iterations 
in each loop depends on the size of the input list.

In bubble sort, for a list of length n, the outer loop runs n times to ensure that every element is 
compared and moved to its correct position.Within each iteration of the outer loop, the inner loop also 
runs n times in the worst case. In the inner loop, comparisons and swaps are performed between adjacent elements 
to move the larger elements towards the end of the list. """