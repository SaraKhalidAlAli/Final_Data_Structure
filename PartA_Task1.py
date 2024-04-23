#Task 1

#implementing hash table for finding a post by unique datetime value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size


    def _hash(self, key):
        return hash(key) % self.size


    def insert(self, key, value, name):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value, name)]
        else:
            for i, (k, v, n) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value, name)
                    break
            else:
                self.table[index].append((key, value, name))


    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v, n in self.table[index]:
                if k == key:
                    return v, n  #returing the post content and the name of the person
        return None, None  # returning "None" if post is not found

# Example usage to test:
if __name__ == "__main__":
# creating a hash table with the size 10
    hash_table = HashTable(10)

# Test Case For "Inserting posts with unique datetime values"
    hash_table.insert("2024-04-20 10:00:00", "Post 1", "sara_khalid")
    hash_table.insert("2024-04-20 11:30:00", "Post 2", "dott2001")
    hash_table.insert("2024-04-20 15:45:00", "Post 3", "BobBob")
    hash_table.insert("2024-04-21 08:00:00", "Post 4", "Salma__1")
    hash_table.insert("2024-04-21 13:15:00", "Post 5", "cat6789")
    hash_table.insert("2024-04-22 09:30:00", "Post 6", "maitha_maitha")

# Finding a specific post by "its unique datetime value from the test case"
    post_datetime = "2024-04-20 11:30:00"
    post_content, poster_name = hash_table.get(post_datetime)
    print("--------------------------------------------------------------------------------------------------")
    print("\nFinding a post by its unique datetime value: ")
    if post_content:
        print(f"\nPost found at {post_datetime} by {poster_name}: {post_content}")
    else:
        print(f"No post found at {post_datetime}")

    print("\n--------------------------------------------------------------------------------------------------")

    # Prompt the user to press Enter to exit
    input("Press Enter to exit...")


