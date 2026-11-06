my_str="万过薪月，员序程马黑来，nohtpy学"
r1=my_str[9:4:-1]
print(r1)
r2=my_str.split("，")
r3=r2[1]
r4=r3.replace("来"," ")
r5=r4[4::-1]
print(r5)
"""
易错；1.中英文输入输出
     2.数下标时从0开始而不是1，结束下标不含
"""