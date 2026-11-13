try:
    with open("test.txt","r",encoding="utf-8")as f:
#易错；1.引号
#     2.补全括号内内容
        content=f.read()
        print("文件打开成功！内容是：")
        print(content)
except FileNotFoundError:
#规范：明确异常类型
    print("文件找不到，正在创建...")
    with open("test.txt","w",encoding="utf-8")as f:
#易错；什么mode下就只能做那件事
        f.write("你好,python!")
        print("文件创建并写入成功！")
        with open("test.txt", "r", encoding="utf-8") as f2:
#区分f
            content=f2.read()
            print(content)


