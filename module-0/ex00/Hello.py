ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# My code----------------------------------------------------

# changing the second element of the list
ft_list[1] = "World!"

# changing the tuple to list
# changing the second element of the new list
# changing it back to a tuple
new_list = list(ft_tuple)
new_list[1] = "Portugal!"
ft_tuple = tuple(new_list)

# removing the item "tutu!" from the set
# adding the item "Lisboa!" to the set
ft_set.remove("tutu!")
ft_set.add("Lisboa!")

# changing the value associated with the key "Hello"
ft_dict["Hello"] = "42Lisboa!"

# -----------------------------------------------------------

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
