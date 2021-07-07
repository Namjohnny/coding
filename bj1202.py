N, K = map(int, input().split())
arrN = []
arrK = []
sum = 0

for i in range(N):
    M, V = map(int, input().split())
    arrN.append([M, V])
for i in range(K):
    C = int(input())
    arrK.append(C)

arrN = sorted(arrN, key = lambda x : -x[1])
arrK.sort()

for n in range(len(arrN)):
    for k in range(len(arrK)):
        if arrN[n][0] <= arrK[k]:
            sum += arrN[n][1]
            arrN[n] = [1000001, 0]
            arrK[k] = 0
print(sum)
