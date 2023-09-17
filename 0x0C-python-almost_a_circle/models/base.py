#!/usr/bin/python3

class Base:
    __nb_objects = 0  # Class variable to track the next available ID

    def __init__(self, value=None):
        if value is not None:
            self.id = value
        else:
            Base.__nb_objects += 1  # Increment the ID counter
            self.id = Base.__nb_objects  # Assign the incremented ID

    def display(self):
        print(f"Value: {self.id}")


if __name__ == "__main__":
    # This code will execute if base.py dis run directly
    base_instance = Base(42)
    base_instance.display()
