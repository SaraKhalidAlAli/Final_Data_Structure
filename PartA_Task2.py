#TASK 2

#defining the class of the tree
class TreeNode:
    def __init__(self, datetime, post, left=None, right=None): #initializing
        self.datetime = datetime
        self.post = post
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, datetime, post):
        self.root = self._insert(self.root, datetime, post)

    def _insert(self, node, datetime, post):
        if node is None:
            return TreeNode(datetime, post)
        elif datetime < node.datetime:
            node.left = self._insert(node.left, datetime, post)
        else:
            node.right = self._insert(node.right, datetime, post)
        return node

    def search_posts_in_range(self, start_datetime, end_datetime):
        posts = []
        self._search_posts_in_range(self.root, start_datetime, end_datetime, posts)
        return posts

    def _search_posts_in_range(self, node, start_datetime, end_datetime, posts):
        if node is None:
            return

        if start_datetime <= node.datetime <= end_datetime:
            self._search_posts_in_range(node.left, start_datetime, end_datetime, posts)
            posts.append((node.datetime, node.post))
            self._search_posts_in_range(node.right, start_datetime, end_datetime, posts)
        elif node.datetime < start_datetime:
            self._search_posts_in_range(node.right, start_datetime, end_datetime, posts)
        else:
            self._search_posts_in_range(node.left, start_datetime, end_datetime, posts)




# Example usage:
if __name__ == "__main__":
    # Create a BST
    bst = BST()

    # Inserting posts with datetime values
    bst.insert("2024-04-20 12:30:00", {"content": "Post 1", "time": "12:30"})
    bst.insert("2024-04-20 13:15:00", {"content": "Post 2", "time": "13:15"})
    bst.insert("2024-04-20 13:30:00", {"content": "Post 3", "time": "13:30"})
    bst.insert("2024-04-20 13:45:00", {"content": "Post 4", "time": "13:45"})
    bst.insert("2024-04-20 14:00:00", {"content": "Post 5", "time": "14:00"})
    bst.insert("2024-04-20 14:30:00", {"content": "Post 6", "time": "14:30"})

    print("\n--------------------------------------------------------------------------------------------")



    #TEST CASE 1: Specifying the time range
    start_time = "2024-04-20 13:00:00"
    end_time = "2024-04-20 14:00:00"

    # Finding posts within the specified time range
    posts_in_range = bst.search_posts_in_range(start_time, end_time)

    print(f"Posts within the time range {start_time} to {end_time}:")
    if posts_in_range:
        for datetime, post in posts_in_range:
            print(f"Datetime: {datetime}, Post: {post['content']}, Time: {post['time']}")
    else:
        print("No posts found within the specified time range.")
