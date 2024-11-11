ft_list = ["Hello", "tata!"] #world
ft_tuple = ("Hello", "toto!") #country
ft_set = {"Hello", "tutu!"} #city
ft_dict = {"Hello" : "titi!"} #name

ft_list[1] = "World"

tuple_list = list(ft_tuple)
tuple_list[1] = "Germany"
ft_tuple = tuple(tuple_list)

ft_set.remove("tutu!")
ft_set.add("Wolfsburg")

ft_dict["Hello"] = "42 Wolfsburg"

print(type(ft_list), ft_list)
print(type(ft_tuple), ft_tuple)
print(type(ft_set), ft_set)
print(type(ft_dict), ft_dict)