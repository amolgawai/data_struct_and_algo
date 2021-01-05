""" Permutations and combinations using recursion"""


def combinations(lst):
    """Combinations of elelmets in a list

    Algorithm : -
    Base case - combinations of an empty array is empty double array
    This is a starting point
    After the base case, add every element to the arrays without the element
    and also return the array without element
    Start the recursion by removing the first element of array and getting the
    combinations for the rest of array
    """

    if len(lst) == 0:
        return [[]]

    first_ele = lst[0]
    combi_without_fst = combinations(lst[1:])

    combi_with_first = list()
    for a_combi in combi_without_fst:
        combi_with_first.append(a_combi + [first_ele])

    return combi_without_fst + combi_with_first


def permutations(lst):
    """Permutations of elelmets in a list

    Algorithm : -
    Base case - permutations of an empty array is empty double array
    This is a starting point
    After the base case, add an element at every position of the permutations
    without th element
    Start the recursion by removing the first element of array and getting the
    permutations for the rest of array
    """

    if len(lst) == 0:
        return [[]]

    first_ele = lst[0]
    perm_without_first = permutations(lst[1:])

    perms = list()
    for a_perm in perm_without_first:
        for indx in range(len(a_perm) + 1):
            perm = a_perm[:indx] + [first_ele] + a_perm[indx:]
            perms.append(perm)

    return perms


def main():
    """The main testing function"""

    print(combinations(["a", "b", "c"]))
    print(permutations(["a", "b", "c"]))


if __name__ == "__main__":
    main()
