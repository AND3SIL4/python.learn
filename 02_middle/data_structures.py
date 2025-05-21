"""
NOTES:
    Data structures are a representation of data in memory in order to get better performance
    to manipulate the information inside them. They are design for specific purposes.

    Data structures:
        - Arrays: Arrays are a list of data. It's a list of data that are stored in memory
            - Restrictions:
                - Has consecutive elements
                - Has a fixed size
                - Recommend to use the same type of data

            - Cab be a list of the same type of data or mixed types of data
            - integers are stored in 4 bytes depends on the binary representation
            - chars are stored in 1 byte
            - boolean are stored in 1 byte

        - Linked lists: are a lists of elements that each element points to the next element
                        in memory
            - Restrictions:
                - Can be any type of data
                - No fixed size
                - No consecutive elements
                - Much faster than arrays

            - The first element is called the head
            - The last element is called the tail
            - Each element is called a node

        - Stack: used to perform the undo or redo operations
            - Linear collection of elements
            - Items are inserted and removed in a
            - Has a particular order
            - LIFO: Last In First Out

        - Queue: used to perform the operations of a queue
            - Linear collection of elements
            - Items are inserted and removed in a
            - Has a particular order
            - FIFO: First In First Out

"""

# Arrays or lists
my_list: int = [1, 2, 3, 4, 5]

print(my_list, type(my_list))
