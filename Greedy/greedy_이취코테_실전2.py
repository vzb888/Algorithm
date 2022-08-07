# N,M,K = input().split()
# data = input().split()

N=5
M=8
K=3
data= [2,4,5,4,6]
data.sort(reverse=True)
cnt=0
while True:
    for i in range(K):
        cnt+=data[0]
        M-=1
        if M==0: break
    cnt+=data[1]
    M-=1
    if M==0: break

print(cnt)