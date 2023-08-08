from create_nodes import Node



class SingleLinkedList:
   def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#To convert the single linked list into a binary search tree

     def list_to_bst(self, data_list):
        data_list.sort()  # Sort the input list
        self.head = self._list_to_bst_helper(data_list)

    def _list_to_bst_helper(self, sorted_list):
        if not sorted_list:
            return None

        mid = len(sorted_list) // 2
        root = Node(sorted_list[mid])

        root.left = self._list_to_bst_helper(sorted_list[:mid])
        root.right = self._list_to_bst_helper(sorted_list[mid + 1:])

        return root

#To test the Binary Search Tree


data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

def main():
    linked_list = SingleLinkedList()

    for data in data_list:
        linked_list.insert(data)

    print("Linked List:")
    linked_list.display()

    bst_linked_list = SingleLinkedList()
    bst_linked_list.list_to_bst(data_list)
    print("\nBinary Search Tree:")
    bst_linked_list.display()

if __name__ == "__main__":
    main()