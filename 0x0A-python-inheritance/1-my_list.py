#!/usr/bin/python3

class MyList(list):
    """
    A class that inherits from list and provides additional functionality.

    This class inherits from the built-in list class and adds a method to print
    the list in ascending sorted order.

    Attributes:
        None

    Methods:
        print_sorted: Prints the list in ascending sorted order.

    Example:
        my_list = MyList()
        my_list.append(3)
        my_list.append(1)
        my_list.append(2)
        my_list.print_sorted()
        # Output: [1, 2, 3]
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    # Print the original list
    print(my_list)

    # Print the sorted list using the print_sorted method
    my_list.print_sorted()

    # Print the original list again (should remain unchanged)
    print(my_list)
