class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beganing(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linkedlist(self):
        if self.head == None:
            print("No Elements")
            return
        iter = self.head
        llstr = ""
        while iter:
            suffix = ""
            if iter.next:
                suffix = "-->"
            llstr += str(iter.data) + suffix
            iter = iter.next
        print(llstr)

    def get_length(self):
        iter = self.head
        count = 0
        while iter:
            count += 1
            iter = iter.next
        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        iter = self.head
        while iter.next:
            iter = iter.next

        iter.next = Node(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beganing(data)
            return

        iter = self.head
        count = 0
        while iter:
            if count == index - 1:
                node = Node(data, iter.next)
                iter.next = node
                break
            count += 1
            iter = iter.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        iter = self.head
        count = 0
        while iter:
            if count == index - 1:
                iter.next = iter.next.next
                break
            count += 1
            iter = iter.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            self.insert_at_beganing(data_to_insert)
            return

        if self.head.data == data_after:
            self.head = Node(data_to_insert, self.head.next)
            return

        iter = self.head
        while iter.data != data_after:
            iter = iter.next

        node = Node(data_to_insert, iter.next)
        iter.next = node

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        iter = self.head

        while iter.next:
            if iter.next.data == data:
                iter.next = iter.next.next
                return
            iter = iter.next


if __name__ == "__main__":
    root = LinkedList()
    root.insert_at_beganing(20)
    root.insert_at_beganing(30)
    root.insert_at_beganing(40)
    # # root.insert_after_value(30, 90)
    # # root.print_linkedlist()
    # # print(root.get_length())
    # # root.insert_at_end(50)
    # # root.print_linkedlist()
    # # root.insert_at(3, 60)
    # # root.print_linkedlist()
    # # root.insert_at(0, 160)
    # # root.print_linkedlist()
    # # root.remove_at(5)
    # # root.print_linkedlist()
    # # root.remove_at(0)
    # root.print_linkedlist()

    # # fruits = LinkedList()
    # # fruits.insert_values(["oranges", "greaps", "mangoes"])
    # # fruits.print_linkedlist()
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_linkedlist()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print_linkedlist()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print_linkedlist()
    ll.remove_by_value("figs")
    ll.print_linkedlist()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_linkedlist()
