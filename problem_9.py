#problem_09: connect ropes to minimize the cost.
#[1,2,3,4,5] =># [1,2,3,4,5] =>[3,3,4,5],cost=3 => [6,4,5],cost=6+3=>[6,9],cost=3+6+9=>[15],cost=3+6+9+15=33 will be the ans

import heapq

def sol(arr):
    ans=0
    heapq.heapify(arr)  # small number will be in the top position
    while len(arr)>1:
       # print(arr)
        item1=heapq.heappop(arr) # 1st small
        #print(arr)
        item2=heapq.heappop(arr) #2nd small
        ans+=item1+item2
        heapq.heappush(arr,item1+item2) # add new rope in heap after adding 2 small rope ! 

    return ans

print(sol([5,2,1,4,3]))

