# Find the contiguous sub-array maximum sum.


# Method -1(window Concept)
def maximumSum(arr,n):
    curr_max = arr[0]

    for i in range(n):
        for j in range(i,n):
            curr_max=max(sum(arr[i:j+1]),curr_max)
    return(curr_max)
        




# method -2

def contiguous(arr,n):
    curr_max=arr[0]
    previous_max = arr[0]
    for i in range(1,n):
        curr_max = max(arr[i],arr[i]+curr_max)
        previous_max = max(curr_max,previous_max)
    return previous_max

arr = [-2,-3,-5,-9,-7,-1] 
n = len(arr)
print(contiguous(arr,n))
print(maximumSum(arr,n))
