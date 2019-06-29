"""
Assignment 4
Notes:
•	Read everything in this assignment very carefully and do not miss any steps. Think thoroughly and follow as stated. Use intuition for writing your algorithmic program.
•	Submit your assignment in D2L-> Assignment4.
•	Do not copy from each other. Any sign of cheating is not tolerated and will be reported immediately to the department. Plagiarism will give you an instant zero mark for this assignment.
•	You’d need to have a readme file ready explaining all the procedure and mindset that you followed to complete this assignment. Your readme file should also explain what are the important files and folders and how I can run your code.
•	This assignment is worth 5% of your total mark for this course.
•	Please submit zip file containing all the solution files and the readme file.
Orchestrate Sorting
Part I (1% mark).
Write a program that based on the size of your input list pick a sorting algorithm of the following options.
1-	Selection sort
2-	Insertion sort
3-	Quick Sort
4-	Random sort (that we did in class)
For picking the right choice, you should think of computation time complexity and big O notation that we discussed in class. For example, think of the small lists, which one of the above sorting algorithms are better, and for the bigger ones which one could be the right candidate, for medium sized lists which one….and so on. You can also think of coming up with a method that figures out what percentage of a list needs sorting and apply the right algorithm accordingly. Think about it. Have some discussions with your fellow friends about your design.
You can read this article to get some ideas: https://pmihaylov.com/sorting-algorithms/
Or this one: http://www.cscjournals.org/download/issuearchive/IJCSS/Volume7/IJCSS_V7_I3.pdf#page=35
Part II (3% mark). Performance measurement:
Automate your code such that it measures the lists of following element sizes.
You should measure time that it took the particular sort algorithm to sort the following list with elements as described below. For every row and column you should run the code 1000 times and take the average time of 1000 runs for every box in the following table. For example, for quick sorting, run the code 1000 times for when the number of elements are 100 and record the average time.
Element(s)	Selection sort	Insertion sort	Quick sort	Random sort
1
10
100
1,000
10,000
100,000
1 million
10 million
100 million
1 billion
10 billion
You must create the table above by automating your Python code (2% mark of part II is specified for correct and scalable automation effort). In essence, your code should work with a push button. All of the above should happen by automation. At the end of the program the above Table must be created.
If your sorting effort in any of the boxes above is taking more than 30 minutes, you should quit and record >30min in the box. For example, I am 120% sure that your program would have hard time sorting with random sort that we implemented in class for elements of a list bigger than 100. So you’d have to record >30min if it is taking longer than 30 min for every epoch.
You’d need to report the speed of your computer CPU and the RAM memory space of your computer. For example, you should report that your computer is running at 3.2 GHz, Duo core, with RAM 32 GB, running Windows 10. Scientifically it is important to report your computer specifics so that if someone wants to reproduce your results with the same exact computer, they should be able to do so.
You can measure the run-time of a code snippet using the following link:
https://pythonhow.com/measure-execution-time-python-code/
Use the above link as an example. I am ok if you have a library that captures timing in a more efficient way.
Part III (1%).
Write code to draw the table above. Use legend and different colors for showing different searching algorithms. Use x axis for number of elements in logarithmic scale, and y axis for the time scale.
"""

import random
import time
import csv


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


# Create random list
unsorted = []


def randomlist(elements):
    for i in range(1, elements):
        unsorted.append(random.randint(1, elements))
    return unsorted


# set number of loops (1000 for assignment 4)
# the number of times each element is sorted
num_loops = 1000

numbers = []
element_list = [
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000,
    10000000000]

selection_time = []
insertion_time = []
quick_time = []
random_time = []
xd = 0
list_element = element_list[0]
timer = 2
toolong = 'Over 30 Minutes'

with open('sort_time.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(['elements', 'selection sort', 'insertion sort', 'quick sort', 'random sort'])

while list_element < 100000:
    print(list_element)


    # number of loops
    for h in range(0, num_loops):

        for j in range(0, list_element):
            x = random.randint(0, list_element)
            numbers.append(x)

        s1 = numbers.copy()
        s2 = numbers.copy()
        s3 = numbers.copy()
        s4 = numbers.copy()

    length = list_element

    start = time.time()
    selection_sort(s1)
    end = time.time()
    selection_time.append(end - start)

    start = time.time()
    insertion_sort(s2)
    end = time.time()
    insertion_time.append(end - start)

    start = time.time()
    quick_sort(s3, 0, len(s3) - 1)
    end = time.time()
    quick_time.append(end - start)

    """
    here we can run the same 4 lines of code using random_sort however, i feel 
    that random sort is a waste of time because if we have to run 1000
    iterations in 30 minutes, even in an array of ten elements random 
    sort will go over the 30 minutes. Therefore I excluded it.
    """

    insertion_avg = sum(insertion_time) / len(insertion_time)
    selection_avg = sum(selection_time) / len(selection_time)
    quick_avg = sum(quick_time) / len(quick_time)

    xd += 1

    list_element = element_list[xd]

    with open('sort_time.csv', 'a', newline='') as f:
        csvwriter = csv.writer(f, delimiter=',')
        csvwriter.writerow([list_element, insertion_avg, selection_avg, quick_avg, ''])


    print(' ' + str(list_element), 'Element(s) To Be Sorted', '--', 'Average of', num_loops, 'sortings.')
    print(' insertion sort average:  ', insertion_avg, 'seconds')
    print(' selection sort average:  ', selection_avg, 'seconds')
    print(' quick sort average:      ', quick_avg, 'seconds')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print('Sorting Completed.')
