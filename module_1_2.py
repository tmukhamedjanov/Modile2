first = input()
second = input()
third = input()

if first == second and first == third and second == third :
    print(3)
elif first == second or second == third or third == first :
    print(2)
elif first != second or first != third or second != third :
    print(0)
