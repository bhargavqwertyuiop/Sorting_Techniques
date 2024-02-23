"""The time complexity of selection sort is O(n^2), where n is the number of elements in the input list.
This is because the algorithm involves two nested loops, resulting in quadratic time complexity.
Selection sort repeatedly selects the smallest (or largest) element from the unsorted sublist and 
moves it to its correct position in the sorted sublist.
The algorithm compares each element in the unsorted sublist to find the minimum (or maximum) element.
Overall, selection sort's performance is poor on large lists due to its quadratic time complexity."""

def selection_sort(num):

    for i in range(len(num)):
        min_idx = i
        for j in range(i+1,len(num)):
            if num[j] < num[min_idx]:
                min_idx = j
        temp = num[min_idx]
        num[min_idx] = num[i]
        num[i] = temp
    return num


num = [6,5,4,3,2,1]
result = selection_sort(num)
print(result)


"""Initial State:

List: [64, 34, 25, 12, 22, 11, 90]
At the beginning, the entire list is considered as the unsorted sublist, and the sorted sublist is empty.

First Pass (i=0):
The algorithm starts by considering the first element (64) as the minimum.
It searches through the unsorted sublist to find the minimum element.
It finds 11 as the minimum element at index 5.
It swaps 64 with 11, placing 11 in the first position of the list.
Updated list: [11, 34, 25, 12, 22, 64, 90]

Second Pass (i=1):
Now, the first element (11) is considered as already sorted.
The algorithm searches for the minimum element in the remaining unsorted sublist [34, 25, 12, 22, 64, 90].
It finds 12 as the minimum element at index 3.
It swaps 34 with 12, placing 12 in the second position of the list.
Updated list: [11, 12, 25, 34, 22, 64, 90]

Third Pass (i=2):
Now, the first two elements (11 and 12) are already sorted.
The algorithm searches for the minimum element in the remaining unsorted sublist [25, 34, 22, 64, 90].
It finds 22 as the minimum element at index 4.
It swaps 25 with 22, placing 22 in the third position of the list.
Updated list: [11, 12, 22, 34, 25, 64, 90]

Fourth Pass (i=3):
Now, the first three elements (11, 12, and 22) are already sorted.
The algorithm searches for the minimum element in the remaining unsorted sublist [34, 25, 64, 90].
It finds 25 as the minimum element at index 4.
It swaps 34 with 25, placing 25 in the fourth position of the list.
Updated list: [11, 12, 22, 25, 34, 64, 90]

Fifth Pass (i=4):
Now, the first four elements (11, 12, 22, and 25) are already sorted.
The algorithm searches for the minimum element in the remaining unsorted sublist [34, 64, 90].
It finds 34 as the minimum element at index 0.
No swapping is needed.
List remains unchanged: [11, 12, 22, 25, 34, 64, 90]

Sixth Pass (i=5):
Now, the entire list is sorted.
Final Sorted List:

Sorted list: [11, 12, 22, 25, 34, 64, 90]"""