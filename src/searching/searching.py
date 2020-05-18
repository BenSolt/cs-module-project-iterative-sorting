def linear_search(arr, target):
    # Your code here
    
    for i in range (0,target):
        if (arr[i] == target):
            return i
        


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        # find midpoint. left plus right divide by 2.
        mid = (left + right) // 2
    
    # is mid element equal to our target?
        if arr[mid] == target:
            #return result of mid
            return mid
        # mid element is less than our target
        if arr[mid] < target:
            # midd + 1
            left = mid + 1
        else:
            #mid - 1
            right = mid - 1

#did not find element
    return -1  # not found
