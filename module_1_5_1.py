immutable_var = (1, 2, "a", 3.14)
print(immutable_var)
#immutable_var [0] = 3
# Значения кортежа не могут быть изменены,
# так как это неизменяемая, упорядоченная коллекция,
# которая может содержать в себе разные виды данных.
# Но при этом может хранить в себе изменяемый список
mutable_list = [4, 5, "b", True]
mutable_list[-1] = False
mutable_list.append(8)
mutable_list.extend("Hello")
mutable_list.extend(["qwer", 3])
mutable_list.remove("l")
print(mutable_list)