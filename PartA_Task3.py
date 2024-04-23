#TASK 3

import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, post):
        heapq.heappush(self.heap, (-post['views'], post))

    def get_max_views_post(self):
        if self.heap:
            return self.heap[0][1]  # return the post with the highest number of views
        else:
            return None


