# Cyclically rotate an array by one
# Method -1
def rotate(arr,n):
    for i in range(n-1,0,-1):
        arr[i],arr[i-1] = arr[i-1],arr[i]
    return


# Method -2

def rotate1(arr,n):
    x = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0] = x
    return

arr = [9, 8, 7, 6, 4, 2, 1, 3]
n=len(arr)
rotate(arr,n)
print(arr)
rotate1(arr,n)
print(arr)