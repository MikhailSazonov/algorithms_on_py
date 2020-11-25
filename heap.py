class Heap:
    def __init__(self):
        self.heap = list()
        self.length = 0

    def remove_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.length = self.length - 1
        self.sift_down(0, self.length)

    def sift_up(self, ind):
        while ind > 0 and self.heap[(ind - 1) // 2] > self.heap[ind]:
            self.heap[(ind - 1) // 2], self.heap[ind] = \
                self.heap[ind], self.heap[(ind - 1) // 2]
            ind = (ind - 1) // 2

    def sift_down(self, pos, n):
        while True:
            min_position = pos
            if 2 * pos + 2 < n and self.heap[2 * pos + 2] < \
                    self.heap[min_position]:
                min_position = 2 * pos + 2
            if 2 * pos + 1 < n and self.heap[2 * pos + 1] < \
                    self.heap[min_position]:
                min_position = 2 * pos + 1
            if min_position == pos:
                break
            self.heap[pos], \
                self.heap[min_position] = \
                self.heap[min_position], \
                self.heap[pos]
            pos = min_position

    def insert(self, x):
        self.heap.append(x)
        self.length += 1
        q = self.length - 1
        self.sift_up(q)

    def empty(self):
        if self.length != 0:
            return False
        return True

    def min(self):
        return self.heap[0]


h = Heap()
print("How many requests?")
N = int(input())
for i in range(N):
    r = input().split()
    if r[0] == "insert":
        if r[1].isdigit():
            h.insert(int(r[1]))
            print("Element succesfully added")
        else:
            print("You should enter number")
    elif r[0] == "minimum":
        print("Minimum is", h.min())
    elif r[0] == "remove" and r[1] == "minimum":
        if h.empty():
            print("Nothing to remove")
        else:
            h.remove_min()
            print("Minimum is removed")
    else:
        print("Unknown request")
