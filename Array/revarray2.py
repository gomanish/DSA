array = [1,2,3,4,5,6,7,8]
a = 0
b = len(array)-1
while(a<=b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    a +=1
    b -=1
print(array)

