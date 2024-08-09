#Two right angled hollow triangle
n=int(input())
for i in range(n):
    if i==0 or i==1 or i==n-1:
        print("* "*(i+1)+"    "*(n-i-1)+"* "*(i+1),end="\n")
    else:
        left="* "+"  "*(i-1)+"* "
        middle="  "*(2*n-2*i-2)
        right="* "+"  "*(i-1)+"* "
        print(left+middle+right,end="\n")
#Hollow Butterfly
n=int(input())
for i in range(n):
    if i==0:
        print("* "+"  "*(2*n-2)+"* ",end="\n")
    else:
        top="* "+"  "*(i-1)+"* "+"  "*(2*n-2*i-2)+"* "+"  "*(i-1)+"* "
        print(top,end="\n")
for i in range(n-1,-1,-1):
    if i==0:
        print("* "+"  "*(2*n-2)+"* ",end="\n")
    else:
        top="* "+"  "*(i-1)+"* "+"  "*(2*n-2*i-2)+"* "+"  "*(i-1)+"* "
        print(top,end="\n")
#inverted hollow pyramid
n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1),end="\n")
for i in range(n-1,0,-1):
    if i==1:
        print(" "*(n-i)+"* ",end="\n")
#solid right angled triangle
n=int(input())
for i in range(1,n+1):
    print("  "*(n-i)+"* "*(i),end="\n")
#inverted right triangle
n=int(input())
print("* "*(2*n-1))
for i in range(1,n+1):
    print("  "*(2*i)+"* "*(2*n-2*i-1))
    else:
        print(" "*(n-i)+"* "+" "*(2*i-4)+"*",end="\n")
#solid right angled triangle
n=int(input())
for i in range(1,n+1):
    print("  "*(n-i)+"* "*(i),end="\n")
#striped rectangle
m=int(input())
n=int(input())
for i in range(1,m+1):
    if(i%2==0):
        print("- "*n,end="\n")
    else:
        print("+ "*n,end="\n")
#Number diamond
n=int(input())
for i in range(1,n+1):
    out=""
    for j in range(1,i+1):
        out=out+str(j)+" "
    print(" "*(n-i)+out,end="\n")
for i in range(1,n):
    out=""
    for j in range(1,(n-i)+1):
        out=out+str(j)+" "
    print(" "*i+out,end="\n")
#Half pyramid
m=int(input())
n=int(input())
s=m-1
for i in range(n,0,-1):
    s+=i
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(s),end=" ")
        s-=1
    print()
#alphabet pyramid
n=int(input())
s=65
for i in range(n):
    for j in range(i+1):
        print(chr(s),end=" ")
        s=s+1
    print()
    s=65
#Albhabets in hollow diamond
n=int(input())
s=65
for i in range(n):
    print(" "*(n-i-1),end="")
    if i==0:
        print('A',end="\n")
        s+=1
    else:
        print(chr(s)+" "*(2*i-1)+chr(s+1),end="\n")
        s+=2
s=s-4
for i in range(1,n):
    print(" "*i,end="")
    if i==n-1:
        print('A',end="\n")
        s+=1
    else:
        print(chr(s)+" "*(2*n-2*i-3)+chr(s+1),end="\n")
        s-=2
    
