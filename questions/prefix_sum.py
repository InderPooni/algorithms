def prefixSum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    
    return arr

print(prefixSum([10,20,30,40,50]))