class Solution:
    ans = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(r, c, i, visited):
            if (r, c) in visited:
                return
            if i==len(word):
                self.ans = True
                return
            visited.add((r, c))
            for dr, dc in directions:
                tr, tc = r+dr, c+dc
                if tr>=0 and tc>=0 and tr<rows and tc<cols and board[tr][tc] == word[i]:                    
                    dfs(tr, tc, i+1, visited)
            visited.remove((r, c))
            return

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    dfs(i, j, 1, set())
        return self.ans
