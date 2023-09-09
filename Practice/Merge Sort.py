s = [1,7,2,9,8,3,4,5,6,5] # len = 9

def MergeSort(nums):
    if not nums:
        return None
    else:
        if len(nums) == 1:
            return nums
        
    l = 0
    r = len(nums) - 1
    m = (r - l) // 2

    # print(nums, l, r, m)

    la = MergeSort(nums[:m+1])
    ra = MergeSort(nums[m+1:])
    res = []

    while la and ra:
        if la[0] < ra[0]:
            res.append(la[0])
            la.pop(0)
        else:
            res.append(ra[0])
            ra.pop(0)

    if ra:
        res.extend(ra)

    if la:
        res.extend(la)

    return res
        

print(MergeSort(s))