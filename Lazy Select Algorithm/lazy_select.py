from random import sample
from math import ceil, floor, sqrt


def lazy_select(S, k, max_iters=200):

    # Handle max recursion depth
    if max_iters == 0:
        raise Exception('Maximum number of iterations reached, failed to find the k-th smallest element')

    # number of elements in the set S
    n = len(S)

    # random subset of S with n^(3/4) elements
    R = sample(S, ceil(n**(3/4)))

    # Sort R using a deterministic optimal sorting algorithm
    R.sort()

    # x is a value used to determine the range of values in R to consider
    x = k * n**(-1/4)

    # l is the lower bound of the range of values in R to consider
    l = max(floor(x - sqrt(n)), 1)

    # h is the upper bound of the range of values in R to consider
    h = min(ceil(x + sqrt(n)), len(R) - 1)

    a = R[l - 1] # a is the lower bound value in R

    b = R[h - 1] # b is the upper bound value in R

    # rank of a in S
    r_a = sum(x < a for x in S)

    # rank of b in S
    r_b = sum(x <= b for x in S)

    if n**(1/4) <= k <= n - n**(1/4):

        # P is a subset of S with values between a and b
        P = [x for x in S if a <= x <= b]

        # If |P| is less than or equal to 4n^(3/4) + 2
        if len(P) <= 4 * n**(3/4) + 2:
            # if S(k) belongs to P
            if r_a <= k <= r_b and k - r_a <= len(P): 
                # we can sort P and return the kth smallest element
                return sorted(P)[k - r_a - 1]

    # If k is not in the specified range or |P| is greater than 4n^(3/4) + 2, repeat the process
    return lazy_select(S, k, max_iters - 1)