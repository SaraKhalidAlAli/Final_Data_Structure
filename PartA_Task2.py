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