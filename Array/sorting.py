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

# Method-3
arr = [0,2,1,2,0]
n= len(arr)
c0=0
c1=0
c2=0
for i in range(n):
    if arr[i]==0:
        c0+=1
    elif arr[i]==1:
        c1+=1
    else:
        c2+=1
for i in range(c0):
    arr[i]=0
for i in range(c0,c0+c1):
    arr[i]=1
for i in range(c0+c1,c0+c1+c2):
    arr[i]=2
print(arr)


# Method-3
#Dutch National flag algorithm
arr = [0,2,1,2,0]
low = 0
mid = 0
high = len(arr)-1
while mid<=high:
    if arr[mid]==0:
        arr[low],arr[mid]=arr[mid],arr[low]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
print(arr)