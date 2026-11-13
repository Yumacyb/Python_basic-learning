my_list=[{"姓名":"熊大","分数":99},
         {"姓名":"熊二","分数":2},
         {"姓名":"光头强","分数":3}
]
for student in my_list:
    if student["分数"]>90:
        print(f"{student['姓名']}分数是{student['分数']}，优秀!")