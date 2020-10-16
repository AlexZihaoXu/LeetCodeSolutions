# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: 'List[Node]' = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node', visited={}) -> 'Node':
        if not node:  # For the case of no node
            return None

        if node in visited:
            return visited[node]  # Execute when circle complete

        clone = Node(node.val)
        visited[node] = clone  # add the present node into visited to prevent looping

        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor, visited))  # Add neighbors and start recursion

        return clone  # Return the completed individual node
