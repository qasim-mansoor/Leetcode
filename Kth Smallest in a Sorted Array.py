class Solution(object):
    
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        i = 0

        def MergeSort(i): # len = 3

            if i == len(matrix) - 1:
                return matrix[i]
            elif(i > len(matrix) - 1):
                return None

            l = MergeSort(i*2) # MergeSort(2)
            r = MergeSort(i*2 + 1) # MergeSort(3)

            print(l , r)

            il, ir = 0, 0
            sa = []

            if l and r:
                while(il < len(l) and ir < len(r)):
                    if l[il] <= r[ir]:
                        sa.append(l[il])
                        il += 1
                    else:
                        sa.append(r[ir])
                        ir += 1

                if il < len(l):
                    sa.extend(l[il:])
                elif ir < len(r):
                    sa.extend(r[ir:])

            if not l:
                return r
            elif not r:
                return l
            else:
                return sa
        
        return MergeSort(1)



print(Solution().kthSmallest([[0,0,0],[0,0,0],[1 ,3 ,5 ],
                              [6 ,7 ,12],
                              [11,14,14]], 3))