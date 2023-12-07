
#5
def unique(ml):
    m=[]
    for x in ml:
        if x in m:
            continue
        else:
            m.append(x)
    return m


mylist = [1, 1, 2, 1, 3, 2, 3] 
print(unique(mylist)) 






'''
#4
cnt=0
def evenCounter(ml):
    global cnt
    for i in ml:
        if i%2==0:
            cnt+=1
    return cnt

mylist = [1, 10, 2, 4, 6] 
evens = evenCounter(mylist) 
print(evens)
'''
'''
#3
mx=0
def maxList(ml):
    return max(ml)

mylist=[1,3,2]
print(maxList(mylist))
'''
'''
#2
def three(a):
    return a%3==0

print(three(4))
print(three(3))
'''
'''
#1
def circle(r):
    s=3.14*r**2
    return s

print(circle(4))
print(circle(1))
'''