class Solution:
    def __init__(self):
        pass

    def build_array_from_permutation(self, nums):
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        
        return res
    
    def getConcatenation(self, nums):
        n = len(nums)
        
        res = [0] * (2*n)
        
        for i in range(len(nums)):
            res[i], res[i + n] = nums[i] , nums[i]
        
        return res
    
    def shuffle_array(self , nums, n):
        res = [0] * (2*n)

        # loop first half of nums and insert x values into the even spots

        even = 0
        odd = 1

        for i in range(n):
            if i % 2 == 0:
                res[even] = nums[i]
                even += 2
            else:
                res[odd] = nums[i + n]
                odd += 2

        return res
    
    def check_if_panagram(self, sentence):
        nums = [False] * 26

        for c in sentence:
            x = ord(c) - 97
            nums[x] = True
        
        for j in nums:
            if not j:
                return False
        
        return True

    # [5,6,7,1,2,3,4] <- [1,2,3,4,5,6,7]
    def rotate(self, nums , k):
        
        nums[::-1]
        self.reverse(nums , 0 , len(nums) - 1)
        self.reverse(nums , 0 , k-1)
        self.reverse(nums, k, len(nums) - 1)

    
    def reverse(self , nums , start , finish):
        while start < finish:
            tmp = nums[start]
            nums[start] = nums[finish]
            nums[finish] = tmp

            start += 1
            finish -= 1


s = Solution()
arr = [1,2,3,4,5,6,7]
s.rotate(arr, 3)

print(arr)
