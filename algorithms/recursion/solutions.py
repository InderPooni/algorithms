from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    #print n -> 1

    def print_n_to_one(self , n):
        if n == 1:
            print(n)
            return
        
        print(n)
        self.print_n_to_one(n-1)

    # print 1 -> n
    def print_one_to_n(self , n):
        if n == 1:
            print(n)
            return
        
        self.print_one_to_n(n-1)
        print(n)
    
    def sort(self , arr: List[int]) -> None:
        # base case
        if len(arr) == 1:
            return
        
        val = arr[len(arr) - 1]

        arr.pop()

        self.sort(arr)
        self.insert(arr , val)

    def insert(self , arr: List[int], element) -> None:
        if len(arr) == 0 or arr[len(arr) - 1] <= element:
            arr.append(element)
        else:

            val = arr[len(arr) - 1]

            arr.pop()

            self.insert(arr , element)

            arr.append(val)

sol = Solution()

arr = [2,5,4,3,9,1]

sol.sort(arr)

print(arr)