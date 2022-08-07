# n,m = int(input().split())
# data=[]
# for i in range(n): data[i]=int(input().split())
n,m=3,3
data=[[3,1,2],[4,1,4],[2,2,2]]

result=[]
for i in range(n):
    data[i].sort()
    result.append(data[i][0])

print(max(result))
