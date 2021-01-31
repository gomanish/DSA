# Move all negative numbers to beginning
# Method-1

arr = [-12, 11, -13, -5, 90,6, -7, 5, -3, -6]
N = len(arr)
i=0
for j in range(0,N):
    if arr[j]<0:
        arr[j],arr[i] = arr[i],arr[j]
        i+=1

print(arr)

# Method-2
# Arrange in incerasing order
