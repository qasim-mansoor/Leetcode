# print(ord('Z') - 64)
s = 'BHX'
# print(26*26 + 25)
# print(26*26 + 26*26 + 26*1 + 1)

col = 0

for i in range(1, len(s) + 1):
    col += (26**(i-1))*(ord(s[-i]) - 64) 

print(col)

#AAA = 703