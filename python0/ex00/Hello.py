ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
a_list = list(ft_tuple)
a_list[1] = "Korea!"
ft_tuple = tuple(a_list)
ft_set.remove("tutu!")
ft_set.add("Seoul!")
ft_dict["Hello"] = "42Seoul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
