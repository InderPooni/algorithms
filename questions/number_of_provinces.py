from typing import List

class Solution(object):

    # Number of connected components
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        if n == 1: return 1

        visited = set()

        def dfs(index):
            visited.add(index)

            for neighbor in range(n):
                if neighbor not in visited and isConnected[index][neighbor] == 1 and (index != neighbor):
                    dfs(neighbor)

            return

        provinces = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1
        

        return provinces

