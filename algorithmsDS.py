#Linear Search algorithm example ------------------------------------------------------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Example usage
numbers = [3, 5, 2, 8, 6, 7, 4]
target_number = 7

result = linear_search(numbers, target_number)

if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found in the list.")
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