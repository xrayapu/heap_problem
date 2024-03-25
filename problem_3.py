# k largest elements on the array 
import heapq 
def sol(arr,k):
    narr=[]
    for num in arr:
        heapq.heappush(narr, num)
        if len(narr)> k:
            heapq.heappop(narr)
            

    return narr

a=[7,5,2,1,4,3,22,12,17]
print(sol(a,3))

# time O(nlogk) | space O(k)

# output : [12,17,22]
