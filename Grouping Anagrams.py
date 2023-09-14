class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        i = 0
        res = []
        while i < len(strs):
            vals = {}
            temp = []
            if strs[i]:
                for char in strs[i]:
                    if char in vals:
                        vals[char] += 1
                    else:
                        vals[char] = 1

                temp.append(strs[i])

            if i < len(strs) - 1:
                j = i+1
                while j < len(strs):
                    
                    print(i)
                    print(strs)
                    dummy = {}
                    if strs[j]:
                        for char in strs[j]:
                            if char in dummy:
                                dummy[char] += 1
                            else:
                                dummy[char] = 1
                        # print(strs[j], vals, dummy)
                        if dummy == vals:
                            temp.append(strs[j])
                            strs[j] = None
                    
                    j += 1

            if temp:
                res.append(temp)
            i += 1
        return res
            

print(Solution().groupAnagrams(['eat', 'ate', 'dress', 'pokemon', 'erssd', 'tea']))
            