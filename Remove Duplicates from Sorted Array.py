nums = [1,1,2]

for i in range(len(nums)-1):
    while(nums[i] == nums[i+1]):
        nums.remove(nums[i+1])
    
    if(len(nums)-2 == i):
        break

count = len(nums)
print(count)
print(nums)