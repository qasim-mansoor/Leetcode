prices = [7,1,5,3,6,4]

l,r = 0,1
maxprofit = 0

while(r<len(prices)):
    if(prices[l]<prices[r]):
        profit = prices[r] - prices[l]
        maxprofit = max(maxprofit, profit)
    else:
        l = r

    r+=1

print(maxprofit)