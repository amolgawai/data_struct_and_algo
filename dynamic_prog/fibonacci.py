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
    num -- the number for which fibonacci number is requestd
    """

    if num in (0, 1):
        return num

    num_tabl = [0] * (num + 1)
    num_tabl[1] = 1
    for indx in range(0, num):
        num_tabl[indx + 1] += num_tabl[indx]
        if not indx == num - 1:
            num_tabl[indx + 2] += num_tabl[indx]

    return num_tabl[num]


def run_algo(algo_tpl, algo_func, msg):
    """Runs the algorith iterating for each item i the input tuple
    Keyword Arguments:
    algo_tpl  -- tuple of algorith inputs
    algo_func -- algorithm function
    msg -- message to print before running algorithm
    """

    print(msg)
    for item in algo_tpl:
        print(f"{item}: {algo_func(item)}")

    print("---------")


def main():
    """The main function"""
    values = (0, 1, 2, 3, 8, 25, 50, 100, 300)

    msg1 = "fibonacci numbers with brute force algorithm"
    run_algo(tuple(filter(lambda x: x <= 8, values)), fib_rec_memoize, msg1)

    msg2 = "fibonacci numbers with memoization algorithm"
    run_algo(values, fib_rec_memoize, msg2)

    msg3 = "fibonacci numbers with tabulation algorithm"
    run_algo(values, fib_itr, msg3)


if __name__ == "__main__":
    main()
