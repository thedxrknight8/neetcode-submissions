class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # you iterate through edges and mark which were visited 
        # if you go to a neighbor that has already been visited
        # then you have a cycle
        # so if you get that point, then select that edge
        # and do that for every edge
        graph = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True
            
            ret = False

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    ret |= dfs(neighbor, target, visited)
            
            return ret


        for u, v in edges:
            if dfs(u, v, {u}):
                return [u, v]
            
            graph[u].append(v)
            graph[v].append(u)

        return []
        