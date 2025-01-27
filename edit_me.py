#lists for testing
mylist = [1, 1, 3, 100]
mylist1 = [11, 1, -9, -10]
mylist2 = [2, 3, 2, 3]

def isincreasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def isdecreasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True

def monotonic(lst):
    return isincreasing(lst) or isdecreasing(lst)

print(monotonic(mylist))  
print(monotonic(mylist1)) 
print(monotonic(mylist2))  