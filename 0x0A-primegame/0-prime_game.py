#!/usr/bin/python3
"""doc doc doc"""


def isWinner(x, nums):
    """doc doc doc"""
    def sieve(n):
        """doc doc doc"""
        primes = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes[p]]

    def play_game(n, primes):
        """doc doc doc"""
        available = [True] * (n + 1)
        turn = 0  # Maria starts
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                for i in range(prime, n + 1, prime):
                    available[i] = False
                turn = 1 - turn  # switch turn
        return turn

    primes = sieve(max(nums))
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_game(n, primes)
            if winner == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
