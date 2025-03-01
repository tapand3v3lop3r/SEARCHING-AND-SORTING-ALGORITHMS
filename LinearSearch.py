def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1


arr = [10, 60, 57, 89, 46]
target = 57
result = linear_search(arr, target)
print(f"Element found at index: {result}" if result != 1 else "Element not found")
print(f"Element found at position: {result+1}" if result != 1 else "Element not found")

