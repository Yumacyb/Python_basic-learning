#通过下标索引取出对应位置的数据
my_list=["A","B","C"]
#列表[下标索引]，从前往后从0开始，从后往前从-1开始
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
#取出嵌套列表的元素
her_list=[[1,2,3],[4,5,6]]
print(her_list[1][1])
#注意；通过下标索引取数据，不能超出范围，否则报错
"""
易错：1.[1]对应第二个元素
"""

