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