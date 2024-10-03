grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
average_point = {}
average_grades = [sum(grades[0]) / len(grades[0]),
                 sum(grades[1]) / len(grades[1]),
                 sum(grades[2]) / len(grades[2]),
                 sum(grades[3]) / len(grades[3]),
                 sum(grades[4]) / len(grades[4])]
average_point.update({students_sort[0] : average_grades[0],
                      students_sort[1] : average_grades[1],
                      students_sort[2] : average_grades[2],
                      students_sort[3] : average_grades[3],
                      students_sort[4] : average_grades[4]})
print(average_point)