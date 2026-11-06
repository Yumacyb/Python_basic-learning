my_str="itheima itcast buxuegu"
r1=my_str.count("it")
r2=my_str.replace(" ","|")
r3=r2.split("|")
print(r1)
print(r2)
print(r3)
"""
易错；1.字符串方法不会改原字符，而是返回一个新结果，要么用变量接住结果，要么直接print()
"""