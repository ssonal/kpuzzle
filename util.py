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


