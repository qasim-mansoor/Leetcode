# Remember, all submissions are being checked for plagiarism.
# Your recruiter will be informed in case suspicious activity is detected.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    
    #Create a hashmap where key is the sum of the digits and value is the index where it was first found
    vals = {}
    maxsum = -1
    
    for i in range(len(A)):
        digitsum = 0
        x = A[i]
        while(x > 0):
            digitsum += x%10
            x = x//10
        # print(digitsum)

        if digitsum in vals:
            #Assuming there could be more than 2 numbers with equal summed digits
            #If a bigger number with same digit sum appears, we replace the index in our hashmap for that key
            maxsum = max((A[vals[digitsum]] + A[i]), maxsum)
            if(A[vals[digitsum]] < A[i]):
                vals[digitsum] = i
        else:
            vals[digitsum] = i
        
    return maxsum


print(solution([51, 42, 17, 71]))