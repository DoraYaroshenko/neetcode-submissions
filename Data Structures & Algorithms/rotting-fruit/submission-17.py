class Solution:
    def bfs(self, rotten_fruits,grid):
        n = len(grid)
        m = len(grid[0])
        distances={}
        queue = deque()
        checked = set()
        for i,j in rotten_fruits:
            queue.append((i,j))
            distances[(i,j)]=0
        while queue:
            i,j = queue.popleft()
            neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)];
            valid_neighbors = [(i,j) for i,j in neighbors if (0<=i<n and 0<=j<m and grid[i][j]==1 and (i,j) not in checked)]
            print(f'{i=},{j=},{valid_neighbors=},{checked=},{queue=}\n')
            for k,l in valid_neighbors:
                grid[k][l]=2
                distance = distances[(i,j)]+1
                checked.add((i,j))
                queue.append((k,l))
                distances[(k,l)]=distance
        return distances

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rotten_fruits = []
        fresh_fruits = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rotten_fruits.append((i,j))
                if grid[i][j]==1:
                    fresh_fruits.append((i,j))
        # print(fresh_fruits)
        if len(fresh_fruits)==0:
            return 0
        distances = self.bfs(rotten_fruits,grid)
        # print(distances)
        still_fresh = [(i,j) for (i,j) in fresh_fruits if (i,j) not in distances]
        if still_fresh:
            return -1
        return max(distances.values())