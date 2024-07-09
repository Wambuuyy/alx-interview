#!/usr/bin/python3
"""find minimum perations to achieve desired"""


def minOperations(n):
    """
        check if nis zero or less
        initialize operations=0 and factor=2
        loop unntil the n is 1
        if its divisible by factor add the factor
        to the number of oprations later after exit of
        loop return no of operations
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
