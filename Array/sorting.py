# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# Method -1

arr = [0,2,1,2,0]
arr1=[]
for i in arr:
    if i==0:
        arr1.append(0)
for i in arr:
    if i==1:
        arr1.append(1)
for i in arr:
    if i==2:
        arr1.append(2)
print(arr1)   

# Method-2
