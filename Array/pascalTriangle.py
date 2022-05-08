def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    arr = [[1],[1,1]]
    if(numRows ==1):
        return [[1]]
    elif(numRows == 2):
        return arr
    else:
        for i in range(1,numRows-1):
            temp = [1]
            for j in range(len(arr[i])-1):
                temp.append(arr[i][j]+arr[i][j+1])
            temp.append(1)
            arr.append(temp)
        return(arr)

print(generate(5))
# output= [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]