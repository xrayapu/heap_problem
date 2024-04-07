# problem 5 : find k closest numbers/elements
import heapq

def sol(arr, k, x):
    
    min_heap = [(abs(x - num), num) for num in arr]
    ans=[]
    heapq.heapify(min_heap)   
    for _ in range(k):
        it=heapq.heappop(min_heap)[1] 
        ans.append(it)

    return ans


# arr = [1,2,3,4,5]
# k = 4
# x = 3

# print(sol(arr,k,x)
