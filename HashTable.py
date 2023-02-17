"""
HASHMAP built with an array of Linked Lists

Hash Map built with hashing the key and hash(key) % array_size to map the key to an index and added to a singly linked list. A key value pair is retrieved by hashing the key again and finding the index followed by finding the key in the linked list. 
"""

class Node():
    def __init__(self, key=None, value=None, next_node = None):
        self.key = key
        self.value = value
        self.next_node = next_node

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    # Iterate through the Linked List
    def iterate(self):
        current = self.head
        while(current):
            print("{}: {}".format(current.key, current.value), end=" --> ")
            current = current.next_node
    
    # Insert a node in the end
    def insert_node(self, key, value):
        new_node = Node(key, value)
        if(self.head):
            current = self.head
            while(current.next_node):
                current = current.next_node
            current.next_node = new_node
            self.size = self.size + 1
        else:
            self.head = new_node
            self.size = self.size + 1

    # Search for key
    def search(self, key):
        current = self.head
        while(current):
            if current.key == key:
                return current.value
            else:
                if current.next_node == None:
                    return None
                else:
                    current = current.next_node

class HashMap():
    def __init__(self, size):
        self.size = size
        self.hashmap = [ LinkedList() for _ in range(size)]

    # Add key|value to hashmap
    def insert(self, key, value):
        index = hash(key) % self.size
        print("INSERT -- {} : Index - {}".format(key, index))
        self.hashmap[index].insert_node(key, str(value))
    
    # Search for value in hashmap with key
    def search(self, key):
        index = hash(key) % self.size
        print("SEARCH -- Index - ", index)
        val = self.hashmap[index].search(key)
        if val == None:
            return "No value found"
        else:
            return val

    # Return index of the key to print it in GUI
    def index(self, key):
        index = hash(key) % self.size
        return index

    # Print hashmap index value
    def printIndex(self, index):
        print("\nIndex - ",index)
        self.hashmap[index].iterate()

def main():
    hashmap = HashMap(50)
    hashmap.insert("hi", "abc")
    hashmap.insert("bye", "xyz")
    index1 = hashmap.index("bye")
    hashmap.printIndex(index1)
    hashmap.printIndex(22)
    retVal = hashmap.search("hi")
    print("hi == ", retVal)
    retVal1 = hashmap.search("awdadao")
    print("awdadao == ", retVal1)

if __name__ == "__main__":
    main()
