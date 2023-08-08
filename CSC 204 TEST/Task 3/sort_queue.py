#using mergesort to sort the queue

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Sorting the queue
def sort_queue(queue):
    arr = []
    while True:
        data = queue.dequeue()
        if data is None:
            break
        arr.append(data)
    sorted_arr = merge_sort(arr)
    for item in sorted_arr:
        queue.enqueue(item)

# Run the sorted queue
queue = Queue()
queue.enqueue(30)
queue.enqueue(10)
queue.enqueue(50)
queue.enqueue(20)
print("Before sorting:")
queue.display()
sort_queue(queue)
print("After sorting:")
queue.display()
