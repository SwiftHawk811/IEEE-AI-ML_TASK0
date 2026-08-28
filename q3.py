N = int(input())
def is_prime(n):
    if n <= 1:
        return False
    # Any number greater than sqrt(n) cannot be a factor of n, if there is no factor found up to sqrt(n), then n is prime.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, N+1):
    if is_prime(i):
        print(i, end=' ')