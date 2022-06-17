N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for _ in range(K):
    if(A[0] < B[-1]):
        A.pop(0)
        A.append(B.pop(-1))


result = sum(A)

print(result)

