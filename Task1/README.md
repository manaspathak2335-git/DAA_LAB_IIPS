LAB Task 1

PART-1

Input:[8,3,15,6,2]

Output: Largest number=15, Number of comparisons = 4, Sorted List:[2,3,6,8,15]

Bubble sort algorithm used in sorting of list and Linear scan is implemented to find largest number

The linear scan used for finding largest number provides best efficiency in finding largest number, Its time complexity is O(N), so efforts grow proportionally as size grows
Bubble sort on another hand has worse case time complexity of O(N^2), so efforts increase quadratically as Input size increases.

Dry Run:-

Largest=8

n=3, comparison 1: 3>8 False

n=15, comparison 2: 15>8 True, Largest = 15

n=6, comparison 3: 6>15 False

n=2, comparison 4: 2>15 False

The code must check every element atleast once to make sure that any element is not left unchecked in finding the largest number

Sorting steps:-
Initialize the boundary: Set a boundary variable (i) equal to the total length of the list. This tracks the portion of the list that still needs to be sorted.

Begin a new pass: Start a loop for the current sweep through the list. Immediately set a swapped flag to False to monitor whether any elements are moved during this specific pass.

Compare adjacent pairs: Iterate through the unsorted portion of the list from the first index up to i - 1. Compare each element with the one immediately next to it.

Swap out-of-order elements: If the left element is strictly greater than the right element, swap their positions. Set the swapped flag to True to register that the list was modified.

Check for early termination: After the inner loop finishes sweeping through the pairs, evaluate the swapped flag. If no swaps occurred (the flag remains False), the list is perfectly sorted, and the algorithm safely breaks out of the outer loop to stop execution.

Shrink the unsorted portion: Because each completed sweep guarantees that the largest number in the current unsorted section "bubbles" up to its correct final position at the rightmost edge, decrease the boundary variable (i) by 1. This ensures the next pass ignores the already sorted elements at the end.

PART - 2

Input: ["Task1","Task2","Task3","Task4","Task5"]

Output:-

1. Served using stack: ['Task5', 'Task4', 'Task3', 'Task2', 'Task1']
   
2. Served using Queue: ['Task1', 'Task2', 'Task3', 'Task4', 'Task5']

Data Structures used: Stack and Queue implemented using python's in-built deque

As Input size grows computational efforts grow proportionally as program uses un-nested loops to insert and remove elements from stack and queue, each task is processed exactly once in each loop, Time complexity: O(N).

The printer should use queue data structure because it is based upon First In, First out(FIFO) which processes jobs in order which they arrive which is requirement for printer.

Dry Run:-

#Stack push and Enqueue loop

task = Task1, Stack = ["Task1"], Queue = ["Task1"] 

task = Task2, Stack = ["Task1","Task2"], Queue = ["Task1","Task2"] 

task = Task3, Stack = ["Task1","Task2","Task3"], Queue = ["Task1","Task2","Task3"]

task = Task4, Stack = ["Task1","Task2","Task3","Task4"], Queue = ["Task1","Task2","Task3","Task4"]

task = Task5, Stack = ['Task1', 'Task2', 'Task3', 'Task4', 'Task5'], Queue = ['Task1', 'Task2', 'Task3', 'Task4', 'Task5']

#Stack Processing

Loop 1:["Task5"]

Loop 2:["Task5","Task4"]

Loop 3:["Task5","Task4","Task3"]

Loop 4:["Task5","Task4","Task3","Task2"]

Loop 5:["Task5","Task4","Task3","Task2","Task1"]

#Queue Processing

Loop 1:["Task1"]

Loop 2:["Task1","Task2"]

Loop 3:["Task1","Task2","Task3"]

Loop 4:["Task1","Task2","Task3","Task4"]

Loop 5:["Task1","Task2","Task3","Task4","Task5"]
