#Word Triangle
s=input()
for i in range(len(s),-1,-1):
    print(s[:i],end="\n")
#shuffle string
s1=input()
s2=input()
finl=""
for i in range(len(s1)):
    if(i%2==0):
        finl=finl+s1[i]
    else:
        finl=finl+s2[i]
print(finl)
#pythagorous triplets
n=int(input())
pairs=0
for a in range(1,n-1):
    for b in range(a+1,n):
        c=(a**2+b**2)**0.5
        if((int(c)**2==a**2+b**2) and c>b and c<=n):
            pairs+=1
print(pairs)
#armstrong numbers within range
m=int(input())
n=int(input())
count=0
for i in range(m,n+1):
    arm=0
    for j in str(i):
        arm=arm+int(j)**len(str(i))
    if(arm==i):
        print(i,end=" ")
        count=1
if(count==0):
    print("-1")
#sum of non-primes upto n:
n=int(input())
a=[]
sum1=0
flag=True
for i in range(n):
    a.append(int(input()))
for j in a:
    flag=True
    for k in range(2,j):
        if(j%k==0):
            flag=False
            break
    if(flag == False):
        sum1=sum1+j
print(sum1)
#Replace with next alphabet
s=input()
t=""
for i in s:
    if i==" ":
        t=t+" "
    else:
        t=t+chr(ord(i)+1)
print(t)
#Temperature coversion
n=input()
val=float(n[:len(n)-1])
deg=n[len(n)-1]
if deg=="C":
    C=val
    F=round(((C*(9/5))+32),2)
    K=round(val+273,2)
elif deg=="F":
    C=round((val-32)*(5/9),2)
    F=val
    K=round(C+273,2)
else:
    C=val-273
    F=round(((C*(9/5))+32),2)
    K=val
print(str(C)+'C')
print(str(F)+'F')
print(str(K)+'K')
#camel case to snake case
n=input()
n=n[0].lower()+n[1:]
str=""
for i in n:
    if i.isupper():
        str=str+"_"+i.lower()
    else:
        str=str+i
print(str.strip())