#  Find the Duplicate Number

# Method -1 (FLyods Algorithm)

def flyods(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow==fast:
            break
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[fast]
        if slow==fast:
            break
    return fast





# Method -2 (general method)
def find(arr):
    count = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] not in count:
            count.append(arr[i])
        else:
            return(arr[i]) 

# Method-3 (using hashing)

def findDuplicate(arr):
    count = [0]*len(arr)
    for i in arr:
        if count[i]==1:
            return i
        count[i]=1

# Method-4 (using set)
def Duplicate(arr):
    N = len(arr)
    s = set(arr)
    n = len(s)
    return((sum(arr)-sum(s))/(N-n))




arr = [8,3,1,4,6,7,5,2,4]
#print(findDuplicate(arr))
#print(Duplicate(arr))
print(find(arr))
print(flyods(arr))