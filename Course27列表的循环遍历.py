my_list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<=9:
    if my_list[i]%2==0:
        print(f"{my_list[i]}")
    i+=1
for j in my_list:
    if (j % 2 == 0):
        print(j)
"""
易错；1.循环、判断的缩进问题
     2.判断条件的选择
"""