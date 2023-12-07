
#13 решето эратосфена
def reshetoRes(verh_n):
    resheto=[True]*(verh_n+1)
    resheto[0]= resheto[1]=False #обнуляем
    for i in range(2,int(verh_n**0.5)+1):
        if  resheto[i]==True:
            for j in range(i*i,verh_n+1,i):
                resheto[j]=False
    resheto=[x for x, is_prime in enumerate(resheto) if is_prime]  #нас интересуют значения которые не равны нулю в списке          
    return resheto

verh=100
print(reshetoRes(verh))
print("Hello")
print("main")

'''
#12
import random
import string

def gen_pass(ln_pass):
    words=string.ascii_letters+string.digits #английские буквы в верхнем и нижнем регистре, выдает символы от 0 до 9
    password1=''.join(random.choice(words) for _ in range(ln_pass))
    return password1

len_pass=10
res=gen_pass(len_pass)
print(res)
'''
'''
#11
def palindrom(strs):
    strs=strs.lower()
    strs=strs.replace(' ', '')
    revers_str=strs[::-1]
    return strs==revers_str

st='Plol lolp'
res=palindrom(st)
print(res)
'''
'''
#10
def cnt_w(st, word):
    cnt=st.count(word) #считает буквы
    return cnt

st='Hello world'
res=cnt_w(st, 'l')
print(res)
'''
'''
#9
def sm(nums):
    res=0
    for num in nums:
        res+=num
    return res

numbers =[1,4,6,8,55]
fin=sm(numbers)
print(fin)
'''
'''
#8
a=10
def smn(b):
    a1=a
    return a+b

res=smn(23)
print(res)
'''
'''
#7
cnt=0
def trutoo():
    global cnt
    cnt+=1

trutoo()
print(cnt)
trutoo()
print(cnt)
'''
'''
#6
def resf(*args):
    res=1
    for num in args:
        res*=num
    return res

fin=resf(2,8,8)
print(fin)
'''
'''
#5
def hi(name, age=26):
    print(f"Hello {name}! You age {age}.")

print(hi('Nik'))
print(hi('Ron', 22))
'''
'''
#4
def sm_all(*args): #если не известно колличество чисел
     return sum(args)

res= sm_all(5,8,4,90)
print(res)
'''

'''
#3
def sum_both(a,b):
    return a+b

res=sum_both(6,10)
print(res)
'''
'''
#2процедура
def print_square(num):
    square=num**2
    print(f"Квадрат {num} числа равен {square}")

print_square(4)
'''


'''
#1функция
def average(numbers):
    if len(numbers)==0:
        return 0
    averages=sum(numbers)/len(numbers)
    return averages #вернуть

num=[5,10,15,20,45]
avg=average(num)
print(avg)
'''


'''
def my_fisr_func(name):
    print('hollo '+name)

my_fisr_func('lari')
my_fisr_func('Ron')
'''