a,b,c=map(int, input().split())
abc=a*b*c
m=[]
ma=0
n=int(input())
for i in range(n):
    a1, b1, c1=map(int, input().split())
    if ((a1<= a or a1<=b or a1<=c) and (b1<= a or b1<=b or b1<=c) and (c1<= a or c1<=b or c1<=c)) and abc>=a1*b1*c1:
        abc1=a1*b1*c1
        m.append(abc1)
if m==[]:
    print(0)
    exit()
ma=max(m)
#print(ma)
print(m)