class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(numCourses):
            indegree[i] = 0

        for prereq, course in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)
        
        visited = set()
        q = deque()
        coursesFinished = 0
        
        for course in indegree:
            if indegree[course] == 0:
                q.append(course)
                visited.add(course)
                coursesFinished += 1
        print(coursesFinished)
        print(q)
        
        while q:
            # before you enqueue a neighbor, you have to make sure 
            # that the indegree[neighbor] = 0
            # therefore, when going through neighbors, make that change
            # indegree[neighbor] -= 1

            # visited prevents double decrement by one course

            course = q.popleft()
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    coursesFinished += 1
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return numCourses == coursesFinished

