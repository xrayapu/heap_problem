# problem 6 : top k frequent elements

# leetcode same code ! 

from collections import Counter
import heapq
def sol(arr,k):
    ans=[]
    ans1=[]
    x=Counter(arr)
    for i in x:
        ans1.append((-x[i],i))

    heapq.heapify(ans1)
    for _ in range(k):
        it=heapq.heappop(ans1)[1]
        ans.append(it)

    return ans
# print(sol([1,1,3,4,3,2,2,1],2))
