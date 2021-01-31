# Find Maximun and minimum element of a given array
# ****   Method -1    ***
array = [9,5,1,0,19,9,4,5] 
print(min(array),max(array))


# ****   Method -2    ***

min=array[0]
max = array[len(array)-1]

if min>max:
    min,max = max,min

for i in array[1:]:
    if i<min:
        min=i
    if i>max:
        max=i

print(min,max)


# ***  Method-3   ***

def minmax(arr,low,high):
    if len(array)==1:
        min=arr[low]
        max = arr[high]
        return(min,max)
    elif len(arr)==2:
        if arr[low]<arr[high]:
            min,max = arr[low],arr[high]
        else:
            min,max = arr[high],arr[low]
        return(min,max)
    else:
        mid = int((low+high)/2)
        min1,max1 = minmax(arr,low,mid)
        min2,max2 = minmax(arr,mid+1,high)
        return(min(min1,min2),max(max1,max2))
    
high = len(array)-1
low = 0
print(min,max)

