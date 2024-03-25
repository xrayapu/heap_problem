# kth smallest number on the array 
import heapq # gives minheap implemetation
def sol(arr,k):
    narr=[]
    for num in arr:
        heapq.heappush(narr, -num) # min heap's alternative using (-) sign
        if len(narr)> k:
            heapq.heappop(narr)
            

    return -narr[0]

a=[7,5,2,1,4,3,22,12,17]
print(sol(a,3))

# time O(nlogk) | space O(k)

def sol1(arr,k):
  arr.sort()
  return arr[k-1]
# time O(nlogn) | space O(n) 

# heap time efficient so, we trying to use heap 
