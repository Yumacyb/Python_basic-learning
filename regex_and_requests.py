#导入两个核心库
import requests#发送HTTP网络请求
import re#正则表达式库，用于文本匹配
print("正在获取网页源代码...")
#构建目标网址，实际上是向https://www.bing.com/search?q=test发送请求
#及在必应搜索关键词"text"
url="https://www.bing.com/search"
params={"q":"text"}
#设置请求头，User-Agent伪装成普通的浏览器(Mozilla/5.0),防止被网站识别为爬虫直接拒绝访问
headers={"User-Agent":"Mozilla/5.0"}
#发送GET请求，获取服务器响应
response=requests.get(url,params=params,headers=headers)
#将响应内容提取为纯文本格式（即网页的HTML源代码），存入变量html_text中
html_text=response.text
#提取网站里隐藏的IP地址
ip_pattern=r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
ip_results=re.findall(ip_pattern,html_text)
print(f"找到了{len(ip_results)}个IP地址（仅展示前五个）：")
for ip in ip_results:
    print(ip)
#提取邮箱地址
email_pattern=r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_results=re.findall(email_pattern,html_text)

