from numpy import insert


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        
        iter = self.head
        while iter.next:
            iter = iter.next
        node = Node(data, None, iter)
        iter.next = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index number")

        if index == 0:
            self.insert_at_begining(data)
            return
        
        iter = self.head
        count = 0
        while iter:
            if count == index - 1:
                node = Node(data, iter.next, iter)
                if node.next:
                    node.next.prev = node
                iter.next = node
                break
            iter = iter.next
            count += 1
                
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index number")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1
        
    def checkLinkedListIsEmpty(self) -> bool:
        if self.head is None:
            return True
        return False

    def get_length(self):
        iter = self.head
        count = 0
        while iter:
            count += 1
            iter = iter.next
        return count

    def getLastNode(self) -> Node:
        if self.checkLinkedListIsEmpty():
            return

        iter = self.head
        while iter.next:
            iter = iter.next
        return iter
    
    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self) -> None:
        assert not self.checkLinkedListIsEmpty(), "List is empty."
        iter = self.head
        dllist = ""
        while iter:
            suffix = ""
            if iter.next:
                suffix = "-->"
            dllist += str(iter.data) + suffix
            iter = iter.next
        print(dllist)

    def print_backward(self) -> None:
        assert not self.checkLinkedListIsEmpty(), "List is empty."
        iter = self.getLastNode()
        dlist = ""
        while iter:
            suffix = ""
            if iter.prev:
                suffix = "<--"
            dlist += str(iter.data) + suffix
            iter = iter.prev
        print(dlist)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            self.insert_at_begining(data_to_insert)

        if self.head.data == data_after:
            self.insert_at_begining(data_to_insert)
        
        itr = self.head
        while itr.next:
            if itr.data == data_after:
               node = Node(data_to_insert, itr.next, itr)
               itr.next.prev = node
               itr.next = node
            itr = itr.next
    
    def remove_after_value(self, data_after):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head = self.head.next
            self.head.prev = None
            return
        
        itr = self.head
        while itr.next:
            if itr.data == data_after:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
