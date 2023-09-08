nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

while nums1[0] != 0:
    # print(nums)
    if nums1[0] < nums2[0]:
        nums1.append(nums1.pop(0))
    else: 
        nums1.append(nums2.pop(0))

while nums2:
    nums1.append(nums2.pop(0))
    
while nums1[0] == 0:
    nums1.pop(0)

print(nums1)