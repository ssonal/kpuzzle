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


def hammingDistance(board):
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


def linearConflict(board):
	size = board.getSize()
	lc = 0
	for i in range(size):

		cells = [board.getCell(i,x) for x in range(size)]
		dest = [(tile,(tile-1)%size) for tile in cells if (tile-1)/size == i]

		for m in range(len(dest)):
			for n in range(len(dest)):
				if dest[m][1] > dest[n][1] and dest[m][0]<dest[n][0]:
					lc += 5

	if lc > 0:
		print '1'
	return lc
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


