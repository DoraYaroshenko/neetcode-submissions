class Solution:
    def bfs(self, i: int, j: int, grid: List[List[int]]):
        n = len(grid)
        m = len(grid[0])
        distances={}
        queue = deque()
        checked = []
        queue.append((i,j))
        distances[(i,j)]=0
        while queue:
            i,j = queue.popleft()
            checked.append((i,j))
            neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)];
            valid_neighbors = [(i,j) for i,j in neighbors if (0<=i<n and 0<=j<m and grid[i][j]>0 and (i,j) not in checked)]
            # print(f'{i=},{j=},{valid_neighbors=},{checked=},{queue=}\n')
            for k,l in valid_neighbors:
                distance = distances[(i,j)]+1
                if distance<grid[k][l]:
                    grid[k][l] = distance
                    queue.append((k,l))
                    distances[(k,l)]=distance


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    self.bfs(i,j,grid)
                    # print(grid)
