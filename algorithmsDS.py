#Linear Search algorithm example ------------------------------------------------------------------------
def linear_search(numbers, key):
    for i in range(len(numbers)):
       if (numbers[i] == key):
           return i
    return -1  # not found

# Main program to test the linear_search() method   
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer value: '))
key_index = linear_search(numbers, key)
     
if (key_index == -1):
    print('%d was not found.' % key)
else:
    print('Found %d at index %d.' % (key, key_index))
#--------------------------------------------------------------------------------------------------------

#Binary search algorithm example ------------------------------------------------------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0  # Initialize comparison count

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1  # Increment comparison count

        if arr[mid] == target:
            return mid, comparisons  # Found target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons  # Target not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target_number = 7

index, comparison_count = binary_search(numbers, target_number)

if index != -1:
    print(f"Number found at index {index} with {comparison_count} comparisons.")
else:
    print(f"Number not found. Total comparisons made: {comparison_count}.")
#---------------------------------------------------------------------------------------------------------