# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    #create a hashmap where key is a number and value is the frequency of that number
    vals = {}

    for num in A:
        if num in vals:
            vals[num] += 1
        else:
            vals[num] = 1
        
    maxval = 0
    for key in vals:
        if(key == vals[key]):
            maxval = max(key, maxval)
        
    return maxval



print(solution([1,2,2,3,3,3,4,4,4]))