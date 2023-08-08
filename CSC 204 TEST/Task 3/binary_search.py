#Implementing a binary search algorithm on an unsorted array.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Convert linked list to array

def linked_list_to_array(linked_list):
    arr = []
    current = linked_list.head
    while current:
        arr.append(current.data)
        current = current.next
    return arr

#To run the binar search algorithm on an unsorted array.
linked_list = LinkedList()
# ... Insert elements into the linked list ...
arr = linked_list_to_array(linked_list)
sorted_arr = sorted(arr)
target = 5
index = binary_search(sorted_arr, target)
if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the array.")
