
# problem 10: find total sum between k1 and k2 smallest numbers.

# input : [1,3,12,5,15,11] k1=3 and k2=6

import heapq
def helper(arr,k):
    temp=[]
    for i in arr:
        heapq.heappush(temp,-i)
        if len(temp) > k:
            heapq.heappop(temp)
    return -temp[0]

def sol(arr,k1,k2):
    total=0
    small1= helper(arr,k1)
   
    small2= helper(arr,k2)
    print(small1,small2)
    for num in arr:
        if num > small1 and num< small2:
            total+=num

    return total

print(sol([1,3,12,5,15,11], 3,6 ))
# output: 23
