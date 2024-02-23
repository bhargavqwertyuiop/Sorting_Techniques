#Best-case and Average Time Complexity (O(n log n))
#Worst-case Time Complexity (O(n**2))

def quick_sort(num):
    if len(num) <= 1:
        return num
    
    pivot_idx = len(num) // 2
    pivot = num[pivot_idx]

    left = []
    right = []
    equal = []

    for i in range(len(num)):
        if(pivot < num[i]):
            right.append(num[i])
        elif(pivot > num[i]):
            left.append(num[i])
        elif(pivot == num[i]):
            equal.append(num[i])
    return quick_sort(left) + equal + quick_sort(right)

num = [6,54,3,2,1]
result = quick_sort(num)
print(result)

"""We first check if the length of the input list arr is less than or equal to 1. 
If so, the list is already sorted and we return it as is.
We select the pivot element from the middle of the list.
We then iterate over each element in the list and partition them into three sublists: 
left (containing elements less than the pivot), right (containing elements greater than the pivot), 
and equal (containing elements equal to the pivot).
We recursively call the quick_sort function on the left and right sublists, and 
concatenate the sorted left, equal, and right lists to obtain the final sorted list."""
        