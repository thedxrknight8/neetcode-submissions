class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ordering = []
        indegree = defaultdict(int)
        graph = defaultdict(list)
        visited = set()
        
        for course in range(numCourses):
            indegree[course] = 0
        
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        q = deque()
        for course in indegree:
            if indegree[course] == 0:
                q.append(course)
                ordering.append(course)
                visited.add(course)
        
        while q:
            course = q.popleft()

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    ordering.append(neighbor)
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return ordering if len(ordering) == numCourses else []
            
