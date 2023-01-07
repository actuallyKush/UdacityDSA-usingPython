"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        current = self.head  # calling the first node as current
        counter = 1  # keeping a counter

        if not self.head:
            return None
        # current and counter are less than position, so
        # +1 counter and move to next element
        while current and counter <= position:
            # if counter == position, return current
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        current = self.head  # start by calling the headnode as current
        count = 1  # counter

        if position == 1:  # if the position to add a new element is 1

            # connect the tail of new element to the first node, and
            # assigning the head to the new element
            new_element.next = self.head
            self.head = new_element

        while current:  # while current is true
            # keep going thru the list to find the position
            if count + 1 == position:

                # 0.next connects to 3 | 2.next connects to 0
                new_element.next = current.next
                current.next = new_element
                return

            else:
                # keep searching for position
                count += 1
                current = current.next
                # break

    def delete(self, value):
        """Delete the first node with a given value."""

        current = self.head  # current is assigned the head node (element) i.e which has the head

        # IF THE HEAD IS THE VALUE TO BE DELETED -->
        if current.value == value:  # if value of current node(element) = the value to be deleted!
            self.head = current.next  # self.head is assigned to the next node after current

        # REMOVING NODE FROM BETWEEN THE LINKEDLIST
        else:
            while current:  # while current is true
                if current.value == value:
                    break
                # shifting thru the values
                prev = current
                current = current.next

            # if reached last element (i.e current = current.next, but there is no next)
            if current == None:
                return
            # in eg, prev.next connects to current.next (2.next connects to 3.next = 2--4)
            prev.next = current.next

            # and disabling current
            current = None


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)