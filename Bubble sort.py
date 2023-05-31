def bubble_sort(lst):
    s=0
    c=0
    n=len(lst)
    swap=True
    while swap==True:
        c=+1
        swap=False
        for i in range(1, n):
            if lst[i-1]>lst[i]:
                c=+1
                temp=lst[i-1]
                lst[i-1]=lst[i]
                lst[i]=temp
                swap=True
                s=s+1
        n=n-1
    print(c)
    print(s)
    return lst
        
def make_list():
    import random
    Lst =[]
    size = 320  # size of the list which can be changed (up to 1000)
    for n in range (0, size):
        Lst.append(random.randint(0, 1000))
    return Lst
mylist=make_list()
mylist=bubble_sort(mylist)
print(mylist)
