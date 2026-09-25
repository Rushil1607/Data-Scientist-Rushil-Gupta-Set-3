import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


nums = list(map(int, input("Enter array elements").split()))
k = int(input("Enter kth position"))
result = find_kth_largest(nums, k)
print(f"The {k}-th largest element is: {result}")
