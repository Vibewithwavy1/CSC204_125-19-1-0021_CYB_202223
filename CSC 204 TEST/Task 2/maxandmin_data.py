from node import Node

class SingleLinkedList:
    def __init__(self):
    self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
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


#For the maximum and minimum data in the single linked list

    def find_max_min(self):
        if not self.head:
            return None, None

        max_data = self.head.data
        min_data = self.head.data

        current = self.head
        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next

        return max_data, min_data

#To test the Maximum and Minimum values in the linked list created above


data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

def main():
    linked_list = SingleLinkedList()

    for data in data_list:
        linked_list.insert(data)

    print("Linked List:")
    linked_list.display()

    max_data, min_data = linked_list.find_max_min()
    print("Max Data:", max_data)
    print("Min Data:", min_data)

if __name__ == "__main__":
    main()