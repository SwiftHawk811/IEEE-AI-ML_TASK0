N = int(input())
a = list(map(int, input().split() ))
largest = a[0]
smallest = a[0]
sum = a[0]
even = 0
odd = 0
for val in a[1:]:
    sum += val
    if val > largest:
        largest = val
    if val < smallest:
        smallest = val

for val in a[0:]:
    if val % 2 == 0:
        even +=1
    else:
        odd +=1

b = []
for i in range(N):
    b.append(a[N-1-i])

print("Largest: ", largest)
print("Smallest: ", smallest)
print("Sum: ", sum)
print("Even count: ", even)
print("Odd count: ", odd)
print("Reversed: ", end="")
print(*b, sep=" ")
