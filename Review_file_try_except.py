try:
    with open("test.txt","r",encoding="utf-8")as f:
        content=f.read()
        print("文件打开成功！内容是：")
        print(content)
except FileNotFoundError:
    print("文件找不到，正在创建...")
    with open("test.txt","w",encoding="utf-8")as f:
        f.write("你好,python!")
        print("文件创建并写入成功！")
        with open("test.txt", "r", encoding="utf-8") as f2:
            content=f2.read()
            print(content)

