class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def idk(reci):
            if(reci == len(digits)):
                return None
            
            lets = []
            for i in range(len(nums[digits[reci]])):
                reci += 1
                res = idk(reci)
                reci -= 1
                
                if(res):
                    for st in res:
                        lets.append(nums[digits[reci]][i] + st)
                else:
                    lets.append(nums[digits[reci]][i])
            
            return lets
        
        res = idk(0)
        if(res):
            return res
        else:
            return []

            

print(Solution().letterCombinations("2"))