class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1

        

        while(l <= r):
            mid = (r+l)//2
            if nums[mid] == target:
                l = mid
                r = mid
                # while nums[l] == target:
                #     l -= 1
                # l += 1

                while l > 0:
                    if(nums[l - 1] == target):
                        l -= 1
                    else:
                        break

                # while nums[r] == target:
                #     r += 1
                # r -= 1

                while r < len(nums) - 1:
                    if(nums[r + 1] == target):
                        r += 1
                    else:
                        break

                return [l,r]
            else:
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return [-1, -1]
                
print(Solution().searchRange([5,7,7,8,8,10], 8))