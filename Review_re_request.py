import requests
import re
print("正在潜入官网...")
url="https://www.bigc.edu.cn/"
headers={"User-Agent":"Mozilla/5.0"}
response=requests.get(url,headers=headers)
html_text=response.text
print(f"网页偷取成功！长度是：{len(html_text)}")
pattern=r'href="(.*?)"'
result=re.findall(pattern,html_text)
print(f"找到了{len(result)}个链接！前五个是：")
for link in result[:5]:
    print(link)
