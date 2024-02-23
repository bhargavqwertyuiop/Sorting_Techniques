""""Insertion sort has a time complexity of O(n^2) in the worst case scenario, 
    but it performs efficiently on small lists and is often used when the list is almost sorted because 
    it can be very efficient in that case. Additionally, 
    Insertion sort is an in-place sorting algorithm, 
    meaning it doesn't require additional memory proportional to the size of the input list. """

def inseration_sort(num):
    for i in range(1,len(num)):
        key = num[i]
        j = i-1
        while j>=0 and key<num[j]:
            num[j+1]=num[j]
            j-=1
        num[j+1] = key
    return num

num = [5,4,3,2,1]
result = inseration_sort(num)
print(result)

"""Consider the list [5, 2, 4, 6, 1, 3].

Start with the second element, 2. Compare it with the first element, 5, and swap them if necessary. 
Since 2 is smaller than 5, swap them.

[2, 5, 4, 6, 1, 3]

Consider the third element, 4. Compare it with 5 first. Since 4 is smaller, leave 5 where it is and compare 4 with 2. 
Since 4 is greater, leave it there.

[2, 4, 5, 6, 1, 3]

Move to the fourth element, 6. Since 6 is greater than the previous element 5, 
it's already in the correct position.

[2, 4, 5, 6, 1, 3]

Move to the fifth element, 1. Compare it with each element in the sorted sublist until finding the correct position. 
In this case, it needs to move all the way to the beginning.

[1, 2, 4, 5, 6, 3]

Finally, consider the last element, 3, and insert it into its correct position among the sorted sublist.

[1, 2, 3, 4, 5, 6]"""
