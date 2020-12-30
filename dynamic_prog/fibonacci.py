"""Dynmaic Programmin example with fibonacci series"""
from memoization import cached


def fib_rec_brut_force(num):
    """fibonacci series with brute force
    Keyword Arguments:
    num -- the number for which fibonacci result is required
    """
    if num in (0, 1):
        return num

    return fib_rec_brut_force(num - 1) + fib_rec_brut_force(num - 2)


@cached
def fib_rec_memoize(num):
    """fibonacci series with memoization
    Keyword Arguments:
    num -- the number for which fibonacci number is requestd
    """
    if num in (0, 1):
        return num

    return fib_rec_memoize(num - 1) + fib_rec_memoize(num - 2)


def fib_itr(num):
    """fibonacci series with iterative tabulation
    Keyword Arguments:
    num --
    """
    num_tabl = [0] * (num + 1)
    num_tabl[1] = 1
    for indx in range(0, num):
        num_tabl[indx + 1] += num_tabl[indx]
        if not indx == num - 1:
            num_tabl[indx + 2] += num_tabl[indx]

    return num_tabl[num]


def main():
    """The main function"""
    print(fib_rec_memoize(3))
    print(fib_rec_memoize(6))
    print(fib_rec_memoize(7))
    print(fib_rec_memoize(8))
    print(fib_rec_memoize(50))
    print(fib_itr(8))
    print(fib_itr(50))


if __name__ == "__main__":
    main()
