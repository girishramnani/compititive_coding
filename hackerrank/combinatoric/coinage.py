T = int(input())
S = [1, 2, 5, 10]
for _ in range(T):
    N = int(input())
    L = list(map(int, input().strip().split()))
    A = [0] * (N + 1)
    B = list(A)
    for i in range(min(L[0], N) + 1):
        A[i] = 1
    for i in range(1, 4):
        for j in range(0, L[i] + 1):
            for k in range(N + 1 - j *S[i]):
                B[k + j * S[i]] += A[k]
        for j in range(0, N + 1):
            A[j] = B[j]
            B[j] = 0
    print(A[N])