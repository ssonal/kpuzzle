import heapq


def manhattanDistance(board):
	score = 0
	size = board.getSize()
	for i in range(size):
		for j in range(size):
			tile = board.getCell(i,j)
			if tile == 0:
				continue

			irow = (tile-1)/size
			icol = (tile-1)%size 
			score += abs(i-irow)+abs(j-icol)

	return score


def misplaced(board):
	score = 0
	size = board.getSize()

	for i in range(size):
		for j in range(size):
			tile = board.getCell(i,j)

			if tile == 0:
				continue

			irow = (tile-1)/size
			icol = (tile-1)%size

			if irow == i and icol == j:
				continue
			score += 1

	return score

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
    def  __init__(self):
        self.heap = []

    def push(self, item, priority):
        pair = (priority,item)
        heapq.heappush(self.heap,pair)

    def pop(self):
        (priority,item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


