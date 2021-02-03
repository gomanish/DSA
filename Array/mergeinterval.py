# Merge Intervals
def merge(intervals):
    ans = [intervals[0]]
    for start,end in intervals[1:]:
        if start<=ans[-1][1]:
            ans[-1][1]=max(end,ans[-1][1])
        else:
            ans.append([start,end])
    return ans

    

intervals = [[1,4],[0,0]]
intervals.sort()
print(merge(intervals))
