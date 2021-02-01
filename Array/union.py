# Union of two arrays 
# Method -1

def doUnion(a,b):
    u=[]
    for i in a:
        if i not in u:
            u.append(i)
    for i in b:
        if i not in u:
            u.append(i)
    return(len(u))

def printunion(a,n,b,m):
    u=set()
    for i in a:
        u.add(i)
    for i in b:
        u.add(i)
    return(len(u))



#    Intersection of two array
def dointersection(a,n,b,m):
    count=0
    if n<m:
        for i in a:
            if i in b:
                count+=1
        return(count)
    else:
        for i in b:
            if i in a:
                count+=1
        return(count)










n=5
m=3
a=[1,2,3,4,5]
b=[1,2,3]
print(doUnion(a,b))
print(printunion(a,n,b,m))
print(dointersection(a,n,b,m))