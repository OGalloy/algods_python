from link import Link

class LinkedList:
    def __init__(self):
        self.head = None    

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def add(self, data):
        link = Link(data) #create new Link
        if self.is_empty():
            self.head = link
        else:
            link.next = self.head #add new item to head link
            self.head = link

    def delete_first(self):
        if self.is_empty():
            return None
        temp = self.head
        #remove link beetween first and second items
        self.head = self.head.next
        return temp.data

    def find(self, data):
        if self.is_empty(): #base case
            return False
        current = self.head
        while current.next != None: #iterate over list
            if current.data == data:
                return True
            current = current.next
        if current.data == data:
            return True
        return False

    def delete(self, data):
        if self.is_empty():
            return None
        
        if self.head.data == data:
            data = self.delete_first()
            return data

        current = self.head
        previous = self.head
        while current.next != data:
            if current.data == data:
                previous.next = current.next
                return current.data
            previous = self.head
            current = current.next
        return None

    def __str__(self):
        if self.is_empty():
            return "List[]"
        
        #if self.head.next == None:
        #return f"List[{self.head.data}]"

        current = self.head
        string = "List["
        while current.next != None:
            string += str(current.data) + ", "
            current = current.next
        string += str(current.data) 
        return string + "]"