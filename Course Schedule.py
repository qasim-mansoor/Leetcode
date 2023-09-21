class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        vals = {}
        
        for i in range(len(prerequisites) + 1):
            # print(i)
            for j in range(numCourses):
                if j in vals:
                    continue
                
                found = False
                for pr in prerequisites:
                    if(j == pr[0] and pr[1] not in vals):
                        found = True

                if not found:
                    vals[j] = None
                
                # print(vals)

        if len(vals) >= numCourses:
            return True
        else:
            return False
        