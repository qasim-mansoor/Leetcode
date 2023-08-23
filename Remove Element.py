nums = [3,2,2,3]
val = 3

count = 0
nums3 = []
for num in nums:
    if(num == val):
        nums3.append(num)
    else:
        nums3.insert(0, num)
        count+=1
nums = nums3
print(count)
print(nums)