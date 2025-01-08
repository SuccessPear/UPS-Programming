class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # idea: 1 dictionary, key: prerequisites, value: list of courses
        # loop through the prerequisties [pre, course], if the pre appear in the course list    before, add the course in the list, if the course is the pre of the pre, return false
        pre_dict = {}
        visited = [-1 for _ in range(numCourses)]
        #print(len(visited))
        for pre, course in prerequisites:
            if pre in pre_dict:
                pre_dict[pre].add(course)
                visited[course] = pre
                if course in pre_dict:
                    
                    # join to set and delete the course set
                    for item in pre_dict[course]:
                        visited[item] = pre
                        pre_dict[pre].add(item)
                    pre_dict.pop(course)
                    
            else:
                if visited[pre] == -1:
                    pre_dict[pre] = set()
                    pre_dict[pre].add(course)
                    visited[pre] = pre
                    visited[course] = pre
                    if course in pre_dict:
                        
                        # join to set and delete the course set
                        for item in pre_dict[course]:
                            visited[item] = pre
                            pre_dict[pre].add(item)
                        pre_dict.pop(course)
                # pre appear in one of the set, add source to the set, if source is a key, join two set
                else:
                    idx = visited[pre]
                    pre_dict[idx].add(course)
                    visited[course] = idx
                    if course in pre_dict:
                        # it's a loop so impossible
                        
                        # join to set and delete the course set
                        for item in pre_dict[course]:
                            visited[item] = idx
                            pre_dict[idx].add(item)
                        pre_dict.pop(course)
        if len(pre_dict) > 1:
            return False
        return True

sol = Solution()

n = 3
prerequisites = [[0, 2], [1, 2], [2, 0]]
print(sol.canFinish(n, prerequisites))