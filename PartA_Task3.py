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


#Example:

#TEAST CASE 1:creating a Max Heap
if __name__ == "__main__":
    # Create a Max Heap
    max_heap = MaxHeap()

    # Inserting posts with view counts and the name of the poster
    max_heap.insert({"content": "Post 1", "views": 100, "poster": "User A"})
    max_heap.insert({"content": "Post 2", "views": 200, "poster": "User B"})
    max_heap.insert({"content": "Post 3", "views": 150, "poster": "User C"})
    max_heap.insert({"content": "Post 4", "views": 300, "poster": "User D"})
    max_heap.insert({"content": "Post 5", "views": 250, "poster": "User E"})

    # Retrieve the post with the highest number of views
    max_views_post = max_heap.get_max_views_post()
    print("\n------------------------------------------------------------------------------------------------")
    if max_views_post:
        print(f"The post with the highest number of views is: {max_views_post['content']} with {max_views_post['views']} views, posted by {max_views_post['poster']}.")
    else:
        print("No posts available.")

print("\n------------------------------------------------------------------------------------------------")
