def binarysearch(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:

      mid= (left+right)//2

      if arr[mid] == target:
        return mid

      elif arr[mid] < target:
        left = mid + 1

      else:
        right = mid - 1

    return -1    

arr=[10,35,47,65,1,101,201,78]
target=201

result = binarysearch(arr, target)

if result != -1:
   print("Element is present at index %d" % result)
else:
   print("Element is not present in array")

  
