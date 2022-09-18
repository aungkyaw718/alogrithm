

from turtle import pos


def search(list,n):
    l = 0  #l  mean lower bound and it is first index of the list
    u = len(list)-1 #u mean upper bound and it is last index value of list
    while l <= u :
        mid = (l+u)//2 # "//" give output to int
        if list[mid] == n:
            globals() ['pos'] = mid 
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid

list = [4,7,8,12,45,99]
n = 45
if search( list,n ):
    print("found at ",pos+1)
else:
    print("not found")
