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

# Method -2
# Two pointer Method
arr = [-12, 11, -13, -5, 90,6, -7, 5, -3, -6]
i=0
j=len(arr)-1
while(i<=j):
    if arr[i]<0 and arr[j]<0:
        i+=1
    elif arr[i]<0 and arr[j]>0:
        i+=1
        j-=1
    elif arr[i]>0 and arr[j]>0:
        j -=1
    else:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
print(arr)



# Method-3
# Arrange in incerasing order
