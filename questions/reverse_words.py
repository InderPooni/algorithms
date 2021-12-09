class Solution(object):
    def reverseWords(self, s):
        
        self.reverse(s, 0, len(s) - 1)
        
        startIndex = 0
        
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                self.reverse(s, startIndex, i-1)
                startIndex = i + 1
                
            
        return s

    def reverse(self,s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp

            start += 1
            end -= 1





s = Solution()
print(s.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))