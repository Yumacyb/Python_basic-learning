with open("D:/word.txt","r",encoding="utf-8") as f:
    content=f.read()
    my_list=content.split()
    my_sum=0
    for i in my_list:
        if i=="itheima":
            my_sum+=1
    print(my_sum)

"""
易错：1.复制的路径为左斜杠而不是右斜杠
     2.with open() as f: 后的内容要缩进
     3.不能直接对文件对象调用split,必须先用f.read()拿到文本字符串再调用
补充；1.split(" ")是按单个空格分割，遇到换行不算分隔符，跨行的单词切不开，导致统计出错
     2.改成不带参数的split()会自动把所有空白（空白、换行、tab）都当分隔符，换行也能切开
"""