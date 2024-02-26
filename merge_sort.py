"""
The time complexity of the Merge Sort algorithm is O(n log n) in the worst, best, and average cases. 
This is because the algorithm divides the array into halves recursively until each subarray has only one element, 
and then it merges them back together in a sorted manner. The division process takes O(log n) time, and 
the merging process takes O(n) time. Therefore, the total time complexity is O(n log n)."""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    middle = len(nums) // 2
    left_half = nums[:middle]
    right_half = nums[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half,right_half)


def merge(left,right):
    res = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            res.append(left[left_index])
            left_index +=1
        else:
            res.append(right[right_index])
            right_index += 1


    res.extend(left[left_index:])
    res.extend(right[right_index:])

    return res

nums = [4,2,7,1,9,3]
sorted_arr = merge_sort(nums)
print(sorted_arr)


"""The space complexity of the Merge Sort algorithm is O(n) 
because it requires additional space for the temporary arrays used during the merging process. 
In each recursive call, new arrays are created to hold the divided portions of the original array, 
and during the merging process, additional space is required to store the merged result."""