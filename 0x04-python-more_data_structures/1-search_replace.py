def search_replace(my_list, search, replace):
    new_list = [replace if num == search else num for num in my_list]
    return new_list

# Test the function with the provided example
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)
