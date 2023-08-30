# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here

    #create a hashmap and keep count of each letter
    vals = {}

    for char in S:
        if char in vals:
            vals[char] += 1
        else:
            vals[char] = 1

    oddcount = 0

    for key in vals:
        if vals[key] % 2 == 1:
            oddcount += 1

    if(oddcount >= 2):
        return oddcount - 1
    else:
        return 0

    


print(solution("abcdefg"))