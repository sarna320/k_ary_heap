
# Autor Piort Niedzialek
class Heap:
    def __init__(self, h, bt, et):
        self.heap = h[:]
        self.build_time = bt
        self.extraction_time = et

    def restore_down(self, index, k):
        length = len(self.heap)
        child = [0] * (k + 1)
        while True:
            for i in range(1, k + 1):
                child[i] = k * index + i if k * index + i < length else -1
    
            max_child, max_child_index = -1, 0
            for i in range(1, k + 1):
                if child[i] != -1 and self.heap[child[i]] > max_child:
                    max_child_index = child[i]
                    max_child = self.heap[child[i]]
    
            if max_child == -1:
                break
    
            if self.heap[index] < self.heap[max_child_index]:
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
    
            index = max_child_index

    def restore_up(self, index, k):
        parent = (index - 1) // k
        while parent >= 0:
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
                parent = (index - 1) // k
            else:
                break

    def build_heap(self, n, k):
        for i in range((n - 1) // k, -1, -1):
            self.restore_down(i, k) 

    def insert(self, elem, k):
        self.heap.append(elem)
        n = len(self.heap)
        self.restore_up(n - 1, k)

    def extract_max(self, k):
        max_elem = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        n = len(self.heap)
        self.restore_down(0, k)
        return max_elem

