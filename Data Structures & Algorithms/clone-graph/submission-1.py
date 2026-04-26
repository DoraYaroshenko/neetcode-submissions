"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def bfs(self,node,copy_node):
        visited={}
        if node.neighbors is None:
            return
        queue = deque()
        queue.append((node,copy_node))
        while queue:
            curr=queue.popleft()
            # print(f'Node: {curr[0].val}, copy_node: {curr[1].val}, queue: {queue}, visited: {[x[0].val for x in visited]}')
            for neighbor in curr[0].neighbors:
                if neighbor not in visited:
                    copy_neighbor = Node(val=neighbor.val)
                    curr[1].neighbors.append(copy_neighbor)
                    queue.append((neighbor,copy_neighbor))
                else:
                    curr[1].neighbors.append(visited[neighbor])
            visited[curr[0]]=curr[1]
            print(f'Copy node neighbors: {[x.val for x in copy_node.neighbors]}')

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        copy_node = Node(val=node.val)
        self.bfs(node,copy_node)
        return copy_node