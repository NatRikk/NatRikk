# Selection sort algorithm example -------------------------------------------------------------------------
def selection_sort(numbers):
   for i in range(len(numbers)-1):
      
      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i+1, len(numbers)):
         
         if numbers[j] < numbers[index_smallest]:
            index_smallest = j
      
      # Swap numbers[i] and numbers[index_smallest]
      temp = numbers[i]
      numbers[i] = numbers[index_smallest]
      numbers[index_smallest] = temp

      # Create a list of numbers to sort
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Display the contents of the list
print('UNSORTED:', numbers)

# Call the selection_sort() function
selection_sort(numbers)

# Display the (sorted) contents of the list
print('SORTED:', numbers)
#------------------------------------------------------------------------------------------------------------

# Insertion sort algorithm example --------------------------------------------------------------------------
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
            j -= 1
    
# Create a list of unsorted values    
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Print unsorted list
print('UNSORTED:', numbers)

# Call the insertion_sort function
insertion_sort(numbers)

# Print sorted list
print('SORTED:', numbers)
#------------------------------------------------------------------------------------------------------------

# Shell sort algorithm example ------------------------------------------------------------------------------
def insertion_sort_interleaved(numbers, start_index, gap):
    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
            temp = numbers[j]
            numbers[j] = numbers[j - gap]
            numbers[j - gap] = temp
            j = j - gap

def shell_sort(numbers, gap_values):
    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(numbers, i, gap_value)
#-------------------------------------------------------------------------------------------------------------
            
# Quicksort algorithm example --------------------------------------------------------------------------------
def quicksort(numbers, start_index, end_index):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if end_index <= start_index:
        return
          
    # Partition the list segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    quicksort(numbers, start_index, high)

    # Recursively sort the right segment
    quicksort(numbers, high + 1, end_index)

# Main program to test the quicksort algorithm.
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)

quicksort(numbers, 0, len(numbers)-1)
print('SORTED:', numbers)
#-------------------------------------------------------------------------------------------------------------

# Merge sort algorithm example -------------------------------------------------------------------------------
 
# Radix sort algorithm example -------------------------------------------------------------------------------