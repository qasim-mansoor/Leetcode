# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    asset = True
    # eg: [4,1,2,3]
    # len = 4
    income = 0
    i = 0

    while i < len(A) - 1:
        # Choosing when to sell
        if asset:
            while(A[i] <= A[i+1]):
                print(i)
                i += 1

            income += A[i]
            asset = False
        # Choosing when to buy
        else:
            while(A[i] >= A[i+1]):
                print(i)
                i += 1

            income -= A[i]
            asset = True

        i += 1

    return income%1000000000

print(solution([4,1,2,3]))