#!/usr/bin/python3
"""doc doc doc"""


def isWinner(x, nums):
    """doc doc doc"""
    if not nums or x <= 0:
        return None

    # Sieve of Eratosthenes to generate prime numbers up to max_n
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    maria_wins = 0
    ben_wins = 0

    # Function to count primes less than or equal to n
    def count_primes_up_to(n):
        return sum(1 for p in primes if p <= n)

    # Simulate each round
    for n in nums:
        prime_count = count_primes_up_to(n)

        # Maria wins if prime count is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
