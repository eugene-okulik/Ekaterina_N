my_dict = {"tuple": ("tuple1", "tuple2", "tuple3", "tuple4",
                     "tuple5", "tuple6"),
           "list": ["list1", "list2", "list3", "list4", "list5", "list6"],
           "dict": {"key1": "value1", "key2": "value2", "key3": "value3",
                    "key4": "value4", "key5": "value5", "key6": "value6"},
           "set": {1, 2, 3, 4, 5, 6}}
print(my_dict["tuple"][-1])
my_dict["list"].append("list7")  # new item added to the end of the list
my_dict["list"].pop(1)  # delete "list2"
my_dict["dict"][("i am a tuple",)] = "value7"  # add new item to the dict
my_dict["dict"].pop("key1")  # delete "key1": "value1"
my_dict["set"].add(7)  # add new element to set
my_dict["set"].discard(2)  # delete element 2 from set
print(my_dict)
