def maxsum(arr, windowsize):
    arraysize = len(arr)

    if arraysize < windowsize:
        print("invalid operation")
        return -1

    window_sum = sum(arr[i] for i in range(windowsize))
    max_sum = window_sum

    for i in range (arraysize - windowsize):
      window_sum = window_sum - arr[i] + arr[ i + windowsize ]
      max_sum = max(window_sum, max_sum)

    return max_sum

arr=[2,5,34,56,2,-100,27,45,68]
answer = maxsum(arr, 4)
print(answer)