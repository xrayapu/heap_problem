# frequency sort : sort the array from it's elements frequency

import heapq
from collections import Counter
def sol(arr):
    temp, ans=[],[]
    x= Counter(arr)
    for i in x:
        temp.append((-x[i],i))

    heapq.heapify(temp)
    while temp:
        it, el= heapq.heappop(temp)
        for _ in range(-it):
            ans.append(el)

    return ans

#print(sol([-1,1,-6,4,5,-6,1,4,1]))

##output: [1, 1, 1, -6, -6, 4, 4, -1, 5]
