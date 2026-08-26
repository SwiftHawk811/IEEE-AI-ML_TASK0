N = int(input())
a = list(map(int, input().split() ))
largest = a[0]
for i in range(1, N):
    if a[i] > largest:
        largest = a[i]
