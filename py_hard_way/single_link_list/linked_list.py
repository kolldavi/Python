from node import SingleLinkedListNode


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None


    def push(self, obj):
        node  = SingleLinkedListNode(obj, None)
        """Appends a new value on the end of the list."""
        if self.begin == None:
            # nothing net
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node
            assert self.begin != self.end

        assert self.end.next == None

    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            assert self.end != node
            self.end = node
            next = self.end.next
            self.end.next = None

  
            return next.value
            
    def shift(self, obj):
        """Add at begining"""
        node  = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            temp = self.begin
            self.begin = node
            self.begin.next = temp
            

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin:
            # save the begin
            node = self.begin
            # if we have only one
            if self.begin == self.end:
                # clear begin and end
                self.begin = None
                self.end = None
            else:
                # set begin to begin.next
                self.begin = node.next

            return node.value
        else:
            return None

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        #remove first item
        index = 0
        if obj == self.begin.value:
            self.unshift()
            return index

        node  = self.begin
        
        while node.next != None:
            index += 1
            if node.next.value == obj:
                node.next = node.next.next
                break
            node = node.next

        return index

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        count = 0
        node = self.begin

        while node != None:
            node = node.next
            count = count + 1

        return count
    def get(self, index):
        """Get the value at index."""
 
        if index < 0 or index >= self.count():
            return None

        curr = self.begin
        count = 0
        while count < index:
            curr = curr.next
            count +=1
        
        return curr.value



    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
    
        cur = self.begin
        to_print = ""

        while cur:
            if not (cur is self.end):
                to_print = to_print + str(cur.value) + ", "
            else:
                to_print = to_print + str(cur.value)

            cur = cur.next

        dump_string = f"{mark}:  {to_print}"
        print('dump',dump_string, end=" ")

    def print_list(self):
        node = self.begin
        while node != None:
            print('Item:',node.value)
            node = node.next