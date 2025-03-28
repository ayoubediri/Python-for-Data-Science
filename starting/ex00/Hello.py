"""
I can't use ft_set directly because it is not ordered,
so I need to sort it first.
and format it as a set, this is the only way to get the output I want.
"""
ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Morocco!")
ft_set = {"Hello", "Rabat!"}
ft_dict = {"Hello": "1337!"}
sorted_list = sorted(ft_set)
ft_set = "{'" + sorted_list[0] + "', '"
ft_set += sorted_list[1] + "'}"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
