class Solution:
    def is_safe(self, i,j,grid):
        return 0<=i<len(grid) and 0<=j<len(grid[0])

    def mark_visited(self,grid, i,j):
        stack = []
        pos_cols = [1,-1,0,0]
        pos_rows = [0,0,1,-1]
        stack.append([i,j])
        while stack:
            i,j = stack.pop()
            grid[i][j] = "0"
            for k in range(4):
                if self.is_safe(i+pos_rows[k],j+pos_cols[k],grid) and grid[i+pos_rows[k]][j+pos_cols[k]]=="1":
                    stack.append([i+pos_rows[k],j+pos_cols[k]])

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        islands = 0
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                if y=="1":
                    islands+=1
                    self.mark_visited(grid, i,j)
                    print(grid)
        return islands