#problem 8: K Closest Points to Origin

import math, heapq
def sol(arr, k):
    ans, temp=[],[]
    for i in range(len(arr)):
        it=math.sqrt((arr[i][0]**2 + arr[i][1]**2))
        temp.append((it,arr[i]))

    heapq.heapify(temp)
    for _ in range(k):
        it= heapq.heappop(temp)[1]
        ans.append(it)

    return ans
print(sol([[1,3],[0,1],[5,8],[-2,2]],2))
