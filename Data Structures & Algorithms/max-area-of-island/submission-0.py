class Solution:
    def dfs(self,grid,i,j):
        result=1
        grid[i][j]=0
        if i<len(grid)-1 and grid[i+1][j]==0 and j<len(grid[0])-1 and  grid[i][j+1]==0 and i>0 and grid[i-1][j]==0 and j>0 and grid[i][j-1]==0:
            return result
        if i<len(grid)-1 and grid[i+1][j]==1:
            grid[i+1][j]=0
            result+=self.dfs(grid,i+1,j)
        if j<len(grid[0])-1 and grid[i][j+1]==1:
            grid[i][j+1]=0
            result+=self.dfs(grid,i,j+1)
        if i>0 and grid[i-1][j]==1:
            grid[i-1][j]=0
            result+=self.dfs(grid,i-1,j)
        if j>0 and grid[i][j-1]==1:
            grid[i][j-1]==0
            result+=self.dfs(grid,i,j-1)
        return result

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    island_area=self.dfs(grid,i,j)
                    max_island_area=island_area if island_area>max_island_area else max_island_area
        print(grid)
        return max_island_area