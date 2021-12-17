# Sorting algorithms for D0012E
This is a short list of all the sorting algorithms coverd in the course D0012E. 
This is mainly ment for me but if you manage to find the list, hope it helps you too.


## Insertion sort
  1. Loop thru array.
  2. For every iteration
  3. Move the previous elements that are larger than the current element one step over to the right
  4. return the new array

## Selection sort
  1. Loop thru the array
  2. For every itteration select the smallest element in the remaining array
  3. insert that element at the current index
  4. after loop
  5. return array since it's sorted
## Mergesort
  1. If length of the current list = 1 return the current list
  2. Go to 1. with the left half of the list storing the returned list as left
  3. Go to 2. with the right half of the list storing the returned list as right
  4. merge the two lists
  5. return the merged list
## Quicksort
  1. If start > = end return
  2. set pivot at end
  4. loop until start >= end
  5. loop until we have reached the end of the list or found an element larger than pivot
  6. in each itteration of the loop increment the start pointer 
  8. loop until we have reached the end of the list or found an element smaller than the pivot 
  9. in each itteration of the loop decrement the end pointer
  10. if end < start we have to swap them
  11. go to 4
  12. swap current end pointer and the old pivot so that the pivot winds up in the correct spot
  13. return pivot
  14. go to 1 with the elements in the array before the pivot 
  15. go to 1 with the elements in the array after the pivot
## Heapsort
  1. Convert list to a min heap
  2. Save smallest element from heap in list
  3. remove smallest element from heap
  4. go to 2 if heap is not empty
  5. return new list
## Bucket sort
  1. Declare an empty list of k elements that ill hold the buckets
  2. Store the max value in the array as m
  3. Loop through the array and for every itteration
  4. insert the current value into the list of buckets at the index floor(k*value/m)
  5. after the loop loop through the list of buckets sorting each one of them with merge sort.
  6. return the sorted list.
### Comments
For large buckets merge sort is better, but if the buckets are small insertion sort could be good since there are so few constants

## Counting sort
  1. Declare a hasmap with the indexes ranging from min value to max value
  2. For every element in the input array
  3. increment the counter in the hashmap at the index of itself minus the minimum value
  4. after that loop
  5. loop through each element in the hasmap, and inserting the key a number of times in to the return list eqaul to the value
  6. return the return list
### Comments
Basically uses a hashmap to store the count of each value in the input list. 

## 

