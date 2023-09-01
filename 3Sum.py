class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    temp = []
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp.append(min(nums[i], nums[j], nums[k]))
                        print(nums[k])
                        temp.append(max(nums[i], nums[j], nums[k]))
                        print(temp)
                        if(nums[i] not in temp):
                            temp.append(nums[i])
                        elif(nums[j] not in temp):
                            temp.append(nums[j])
                        else:
                            temp.append(nums[k])

                        if temp not in ans:
                            ans.append(temp)
        
        return ans

print(Solution().threeSum([1,1,-2]))