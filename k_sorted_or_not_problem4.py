def helper(arr, lo, hi,x):
    while lo <=hi:
        mid = (lo+hi)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            hi = mid -1
        else : lo= mid +1


def sol(arr,k):

    temp = [0]* len(arr)
    for i in range(len(arr)):
        temp[i]= arr[i]

   
    temp.sort()
    
    for i in range(len(arr)):
        j= helper(temp, 0, len(arr)-1, arr[i])

        if abs(i-j)> k:
            return "no"
        
    return "yes"


# print(sol([3,2,1,5,6,4,8,7],2)) => yes    

# print(sol([3,2,1,5,6,4,8,7],1)) => no

        
