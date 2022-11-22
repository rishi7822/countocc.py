def count(lst, x):
    count = 0
    for ele in lst:
        if(ele == x):
            count = count + 1
    return count

lst = [8,3,5,6,7,8,88,88,222,44]
x = int(input("enter the num:"))
print("{} occured {} times".format(x,count(lst,x)))