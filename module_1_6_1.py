my_dict = {"Vasya" : 1999, "Egor" : 1990}
print("Dict: ", my_dict)
print("Existing value: ", my_dict.get("Vasya"))
print("Not existing value: ", my_dict.get("Olya"))
my_dict.update({"Sasha" : 1998,
                "Petya" : 1995})
a = my_dict.pop("Egor")
print("Deleted value: ", a)
print("Modified dictionary: ", my_dict)

my_set = {1,2.2,3,False,1,"Hello",5, 3}
print("Set: ", my_set)
my_set.add(("2", 7))
my_set.discard(1)
print("Modified set: ", my_set)