import re
#场景：你抓取了一段黑客留下的日志文本
log_text="黑客IP是192.168.1.100，攻击时间2026-11-11，执行了恶意命令！"

#1.提取IP地址
#解释；\d代表数字，{1，3}代表1到3位数，\.代表真正的点号
ip_pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
result_ip=re.search(ip_pattern,log_text)
print("提取到的IP:",result_ip.group())

#2.提取日期
data_pattern=r"\d{4}-\d{2}-\d{2}"
result_data=re.search(data_pattern,log_text)
print("提取到的日期：",result_data.group())


