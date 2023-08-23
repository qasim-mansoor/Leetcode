nums = [1,2,3,4,5,6,7]
k = 3

for i in range(k):
    val = nums.pop()
    nums.insert(0,val)

print(nums)
    