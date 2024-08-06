import heapq

def priority_queue():
    queue = []

    heapq.heappush(queue, (1, 'B'))
    heapq.heappush(queue, (0, 'A'))
    heapq.heappush(queue, (2, 'C'))

    while queue:
        priority, node = heapq.heappop(queue)
        print("Priority:", priority, "Node:", node)

priority_queue()
