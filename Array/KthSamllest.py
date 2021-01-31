# Kth smallest element
# ** Method-1 **
arr = [7,10,4,3,20,15]
k = 3
N = 6
for i in range(k-1):
    m = min(arr)
    arr.remove(m)
print(min(arr))

# ** Another Method **
using shorting algorithm

