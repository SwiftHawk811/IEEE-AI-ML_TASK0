original = list(map(int, input().split()))
def process_list(numbers):
    a = numbers.copy()
    for value in a[::-1]:
        if value < 0:
            a.remove(value)
    a.append(0)
    a.sort()
    return a
result = process_list(original)
print("Original: ", original)
print("Result: ", result)