def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        if num == search:
            new_list.append(replace)  # Replace the element with the new element
        else:
            new_list.append(num)  # Keep the element unchanged if not equal to the search element
    return new_list

# Test the function with the provided example
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)
