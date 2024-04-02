import heapq
def sol(arr,k):
    heap = arr[:k+1]
    heapq.heapify(heap)
    ans=[]
    for i in range(k+1, len(arr)):
        small = heapq.heappop(heap)
        ans.append(small)
        heapq.heappush(heap, arr[i])

    while heap : # len(heap) !=0:
        item= heapq.heappop(heap)
        ans.append(item)

    return ans
a=[6,5,3,2,8,10,9]

print(sol(a,3)) 

# time: O(nlog k) | space: O(k)
