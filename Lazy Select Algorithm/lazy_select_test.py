from lazy_select import lazy_select
from random import randint, sample

if __name__ == '__main__':
    
    n = 1_000_000
    test_size = 50
    for _ in range(test_size):
        
        # Define the set S 
        S = [randint(-10_000_000, 10_000_000) for _ in range(n)]

        # Define random rank to return
        k = randint(1, n)
        
        # Find the kth smallest element in S
        result = lazy_select(S, k)

        # compare with naive but safe approach
        assert result == sorted(S)[k-1]

    print("Implementation Test passed.")