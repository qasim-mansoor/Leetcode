nums = [0,0,1,1,1,1,2,3,3]
found = False
for i in range(len(nums)-1):
    if(nums[i] == nums[i+1] and not found):
        found = True
    elif(nums[i] == nums[i+1] and found):
        while(nums[i] == nums[i+1]):
            nums.remove(nums[i+1])

        found = False
    else:
        found = False
    
    if(len(nums)-2 == i):
        break

count = len(nums)
print(count)
print(nums)