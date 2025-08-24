def binary_search(mylist, x):
    low = 0
    high = len(mylist) - 1

    while low <= high:
        mid = (high + low) // 2
        midlist = mylist[mid]

        if midlist < x:
            low = mid + 1
 
        elif midlist > x:
            high = mid - 1
 
        else:
            return mid
        
    return -1

# Example
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
 
result = binary_search(mylist, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")