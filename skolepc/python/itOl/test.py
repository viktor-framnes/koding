N = int(input())
h = [0] * N
b = [0] * N
for i in range(N):
    h[i], b[i] = map(int, input().split())
print(max(h))