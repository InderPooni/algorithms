def findKthLargest(nums, k):
    low = 0
    high = len(nums) - 1

    while low <= high:
        pivotIndex = partition(nums, low, high)

        if pivotIndex == len(nums) - k:
            return nums[pivotIndex]
        elif pivotIndex > len(nums) - k:
            high = pivotIndex - 1
        else:
            low = pivotIndex + 1
    return -1

def partition(nums, left, right):
    pivot = nums[right]
    index = left

    for i in range(left, right):
        if nums[i] <= pivot:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1

    nums[index], nums[right] = nums[right], nums[index]

    return index



print(findKthLargest([3,2,1,5,6,4], 2))