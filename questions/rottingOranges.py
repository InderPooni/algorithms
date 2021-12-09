from collections import deque
from typing import Deque


def rottingOranges(grid):
    if not grid:
        return 0
    
    freshOranges = minutes = 0
    rows, cols = len(grid), len(grid[0])
    q = deque()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                freshOranges += 1
            elif grid[i][j] == 2:
                q.append((i,j))
    
    while q and freshOranges > 0:
        size = len(q)

        for _ in range(size):
            r,c = q.popleft()

            for x,y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                m1, m2 = r+x, c+y

                if (0 <= m1 < rows) and (0 <= m2 < cols) and (grid[m1][m2] == 1):
                    grid[m1][m2], freshOranges = 2, freshOranges-1 # fresh orange -> corrupt orange
                    q.append((m1, m2))
        
        minutes += 1
    

    return minutes if not freshOranges else -1


if __name__ == "__main__":
    result = rottingOranges([[1,2]])

    print(result)


