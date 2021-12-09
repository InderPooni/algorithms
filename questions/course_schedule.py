from typing import DefaultDict

# visited: -1,0, 1
def courseSchedule(numCourses, prerequisites):
    if not prerequisites:
        return True
    
    graph = DefaultDict(list)

    visited = {}

    for course, prereq in prerequisites:
        graph[prereq].append(course)

    
    def dfs(node):
        if node in visited:
            if visited[node] == True:
                return False
            else:
                return True
        
        visited[node] = True

        res = True
        for neighbor in graph[node]:
            res = res and dfs(neighbor)

        visited[node] = False

        return res

    
    for i in range(numCourses):
        if i in graph and i not in visited:
            if dfs(i) == False:
                return False
    
    return True



            






courseSchedule(numCourses = 2, prerequisites = [[1,0]])
