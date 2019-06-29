
import random
import time


# selection sort
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp


# insertion sort
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] in correct position
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j = j - 1


# partition for quick sort
def partition(numbers, i, k):
    #  Pick middle element as pivot
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]

    #  Initialize variables
    done = False
    l = i
    h = k
    while not done:
        #  Increment l while numbers[l] < pivot
        while numbers[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h]
        while pivot < numbers[h]:
            h = h - 1
        """  If there are zero or one items remaining,
              all numbers are partitioned. Return h """
        if l >= h:
            done = True
        else:
            """  Swap numbers[l] and numbers[h],
                  update l and h """
            temp = numbers[l]
            numbers[l] = numbers[h]
            numbers[h] = temp
            l = l + 1
            h = h - 1
    return h


# quick sort
def quick_sort(numbers, i, k):
    j = 0
    """  Base case: If there are 1 or zero entries to sort,
          partition is already sorted  """
    if i >= k:
        return
    """  Partition the data within the array. Value j returned
          from partitioning is location of last item in low partition. """
    j = partition(numbers, i, k)
    """  Recursively sort low partition (i to j) and
          high partition (j + 1 to k) """
    quick_sort(numbers, i, j)
    quick_sort(numbers, j + 1, k)


# random sort
def random_sort(number):
    count = 0
    while sorted(number) != number:
        i = random.choice(number)
        j = random.choice(number)
        a, b = number.index(i), number.index(j)
        number[a], number[b] = number[b], number[a]
        count += 1


# ---------- THIS IS PART 1 OF ASSIGNMENT 4 -------------- #

unsorted = []

def sorting(unsorted):
    """
    we can use random sort if the element is 2 or less,
    since it will only swap the list items once at most.
    """

    x = len(unsorted)

    if x < 3:
        sorted = random_sort(unsorted)
    """
    Since the assignment requires us to use selection sort,
    we can use 
    """
    if x < 20:
        sorted = selection_sort(unsorted)
    """
    Because insertion sort is superior to selection sort in 
    small arrays up to 20-30 elements, let us use insertion 
    sort if the array is less than 30 elements long.
    Source: https://www.quora.com/When-should-one-use-Insertion-vs-Selection-sort
    """
    if x < 30:
        sorted = insertion_sort(unsorted)
    """
    Finally for larger arrays we should use quick sort. Quick 
    sort on average will take O(n log n) comparisons to sort items.
    """
    if x > 30:
        sorted = quick_sort(unsorted)

    return sorted

