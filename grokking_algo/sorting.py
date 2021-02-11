"""Various sorting algorithms - Grokking Algorithms."""
import random

# from mytimeit import timing


# @timing
def selectionsort(array):
    """Implementation of Selection sort."""
    sorted_array = []
    temp_array = array[:]

    for __ in range(len(array)):
        sorted_array.append(temp_array.pop(temp_array.index(min(temp_array))))

    return sorted_array


# @timing
def quicksort_worstcase(array):
    """Quicksort with first item as pivot, hence worst case."""
    if len(array) < 2:
        return array

    pivot = array[0]
    lt_pivot = [ele for ele in array[1:] if ele <= pivot]
    gt_pivot = [ele for ele in array[1:] if ele > pivot]
    return (
        quicksort_worstcase(lt_pivot) + [pivot] + quicksort_worstcase(gt_pivot)
    )


# @timing
def quicksort(array):
    """Implementation of Quicksort with random pivot."""
    if len(array) < 2:
        return array

    pivot_indx = random.randint(0, len(array) - 1)
    temp_array = array[:pivot_indx] + array[pivot_indx + 1 :]
    pivot = array[pivot_indx]
    lt_pivot = [ele for ele in temp_array if ele <= pivot]
    gt_pivot = [ele for ele in temp_array if ele > pivot]
    return quicksort(lt_pivot) + [pivot] + quicksort(gt_pivot)


def run_algo(inputs, algo, msg=""):  # pragma: no cover
    """Run a specific algorithm given a list of inputs."""
    print(msg)
    for inpt in inputs:
        print(f"{inpt} -> , {algo(inpt)}")

    print("===========")


def main():  # pragma: no cover
    """Interactive testing function."""
    inputs = (
        [10, 5, 2, 3],
        #    "gibberish",
        [-200, 10, -400, 5000, 60],
        [10.2, 23.5, -55.6, 400.56, -200.0],
    )

    msg1 = "selection sort"
    run_algo(inputs, selectionsort, msg1)

    msg2 = "quicksort"
    run_algo(inputs, quicksort, msg2)

    msg2 = "quicksort_worst"
    run_algo(inputs, quicksort_worstcase, msg2)


if __name__ == "__main__":
    main()
