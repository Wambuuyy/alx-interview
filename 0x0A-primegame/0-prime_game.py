#!/usr/bin/python3
"""doc doc doc"""


def isWinner(x, nums):
    # Sieve of Eratosthenes to find all primes up to the max number in nums
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Logic to simulate the game and determine the winner
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes <= n
        prime_count = sum(1 for p in primes if p <= n)

        # If prime_count is odd, Maria wins (as she starts)
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
