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
#Perfect squares in range of a and b
a=int(input())
b=int(input())
count=0
for i in range(int(a**0.5),int(b**0.5+1)):
    if(i*i<=b and i*i>=a):
        count+=1
print(count)
#inverted hollow pyramid
n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1),end="\n")
for i in range(n-1,0,-1):
    if i==1:
        print(" "*(n-i)+"* ",end="\n")
    else:
        print(" "*(n-i)+"* "+" "*(2*i-4)+"*",end="\n")
#solid right angled triangle
n=int(input())
for i in range(1,n+1):
    print("  "*(n-i)+"* "*(i),end="\n")