class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


# Queue class contains a Node object
class Queue:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last = None

    # Function to add an element data in the Queue
    def enqueue(self, data):
        """
        function for inserting number in queue
        :param data: inserted element
        :return: perform enqueue operation
        """
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def print_queue(self):
        """
        function for displaying Queue element
        :return: list of item in queue
        """
        print("queue elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

    def primes(self, n):
        """
        function for checking prime number
        :param n: last range of number
        :return: prime numbers in that range
        """
        array = [i for i in range(2, n + 1)]
        p = 2

        while p <= n:
            i = 2 * p
            while i <= n:
                array[i - 2] = 0
                i += p
            p += 1

        for num in array:
            if num > 0:
                self.enqueue(num)


if __name__ == "__main__":
    prime_number = Queue()
    p_range = 1000
    prime_number.primes(p_range)
    prime_number.print_queue()





