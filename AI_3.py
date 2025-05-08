def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the smallest value is at index i
        min_index = i
        for j in range(i + 1, n):
            # Greedily choose the smallest element
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")  # Optional: show progress

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)