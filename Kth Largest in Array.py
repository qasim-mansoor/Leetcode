class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        vals = [None] * k
        
        vals[0] = nums[0]

        for i in range(1, k):
            for j in range(len(vals)):
                if nums[i] < vals[j]:
                    vals.insert(j, nums[i])
                    del vals[k]
                    break

        print(vals)

        for i in range(k+1, len(nums)):
            for j in range(len(vals)):
                if nums[i] < vals[0]:
                    break

                if nums[i] < vals[j]:
                    vals.insert(j, nums[i])
                    del vals[0]
                    break

                if nums[i] > vals[j] and j == len(vals) - 1:
                    vals.insert(j+1, nums[i])
                    del vals[0]
                    break

        
        print(vals)

        return vals[0] 
                    
        
print(Solution().findKthLargest([3,2,1,5,6,4], 2))