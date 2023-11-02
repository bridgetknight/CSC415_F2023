import time

# Implementation of Priority Queue in Python
class PriorityQueue(object):
 
	def __init__(self, size=0):
		self.queue = []
		self.size = size

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)
		self.size += 1

	def size(self):
		return size

	# for popping an element based on Priority
	def delete(self):
		try:
			max_val = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max_val]:
					max_val = i
			item = self.queue[max_val]
			self.size -= 1
			del self.queue[max_val]
			return item
		except IndexError:
			print()
			exit()

''' 
Code to use Max Heap Sort algorithm on a Priority Queue
'''
# Function to turn PQ into a max heap
def max_heapify(arr, i, n):
    # Set current index to largest before comparing
    largest = i
    
    # Children
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child is larger
    if left_child < n and arr.queue[left_child] < arr.queue[largest]:
        largest = left_child

    # Check if right child is larger
    if right_child < n and arr.queue[right_child] < arr.queue[largest]:
        largest = right_child

    # Check if current index is largest
    if largest != i:
        arr.queue[i], arr.queue[largest] = arr.queue[largest], arr.queue[i]
        max_heapify(arr, largest, n)

# Function to sort a Priority Queue
def max_heap_sort(arr):
    # Save the size of the Priority Queue
    n = arr.size

    # Build a max heap using non-leaf nodes and put the largest node at the top
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)

    # Iterate through leaf nodes
    sorted_arr = []
    for i in range(n - 1, 0, -1):
        # Swap current element with initial position
        arr.queue[0], arr.queue[i] = arr.queue[i], arr.queue[0]
        # Preserve max heap property with max_heapify(), putting the root in the correct position
        max_heapify(arr, 0, i)

    # Return sorted Priority Queue
    return arr


# Given input list
lst = [3, 5, 1, 2, 5, 4, 6, 3, 1, 5, 9]

# Convert given list to Priority Queue
pq = PriorityQueue()
for i in lst:
    pq.insert(i)
    
# Perform the sorting algorithm
print(f"\nBefore sorting: {pq.queue}")
start = time.time_ns()
max_heap_sort(pq)
end = time.time_ns()
print(f"After max heap sort: {pq.queue}")
print(f"Time taken: {end-start} \n")

