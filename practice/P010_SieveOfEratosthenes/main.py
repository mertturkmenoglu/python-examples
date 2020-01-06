# Prime number finder


def sieve_of_eratosthenes(n: int):
    prime = [True for _ in range(n+1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [i for i in range(2, n) if prime[i]]


print(sieve_of_eratosthenes(50))
