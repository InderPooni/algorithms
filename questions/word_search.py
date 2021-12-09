def wordSearch(board, word):
    rows, cols = len(board), len(board[0])

    visited = set()

    def dfs(r,c,index):
        if index == len(word):
            return True
        
        if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[index]):
            return False

        visited.add((r,c))

        result = (dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1))

        visited.remove((r,c))

        return result

    for x in range(rows):
        for y in range(cols):
            if board[x][y] == word[0]:
                if dfs(x,y,0):
                    return True
    
    return False


print(wordSearch(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))