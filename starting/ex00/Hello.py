ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Morocco!")
ft_set = {"Hello", "Rabat!"}
ft_dict = {"Hello" : "1337!"}

# because the set is not orderI need to make sure 
# that I get the right order every time
my_list_from_set = sorted(list(ft_set))
print(ft_list)
print(ft_tuple)
print(my_list_from_set)
print(ft_dict)