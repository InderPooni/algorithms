# Maximum Sum Subarray of size k
"""
    i and j are two pointer that will make up our window
    to get the right window size the falling equality must be true: k = j - i + 1
    start i , j from 0 , and increment j till it is at the correct window size
    once it is at the correct window size then subsequent sums can be found by subtracting i and moving j and adding it
    compare the sums and maintain a maximum sum for each sub array


"""
def max_sum_subarr_k(arr , k):
    n = len(arr)
    
    if k > n - 1 or k == 0 or n == 0:
        return 0
    
    i , j , max_sum , s = 0, 0, 0, 0

    while j < n:
        s += arr[j]

        if (j - i + 1) < k:
            j += 1
        
        elif (j - i + 1) == k:
            max_sum = max(s , max_sum)

            s -= arr[i]

            i += 1
            j += 1
    
    return max_sum


# Unit tests 

# arr = [2,5,1,8,2,9,1]
# k = 3
# expected = 19

# actual = max_sum_subarr_k(arr , k)

# print(actual == expected)

# # edge case
# print(max_sum_subarr_k([1] , 2) == 0)


"""
First Negative Number in every Window of Size K
"""

def first_neg_of_size_k(arr , k):
    pass