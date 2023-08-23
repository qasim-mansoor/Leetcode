nums = [2,2,1,1,3,3,1,2,3,2,3]

res, count = 0, 0

for n in nums:
    if count == 0:
        res = n

    count += (1 if n == res else -1) 

print(res) 