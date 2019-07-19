#尝试输出hello world
message = "hello world"
print(message)

#字符串拼接
first_name = "inspire"
last_name = "wind"
full_name = first_name + " " + last_name
print(full_name)

#字符串的方法不改变原有字符串
message.upper()
#print(message.upper())
print(message)

message.lower()
#print(message.lower())
print(message)

message.title()
#print(message.title())
print(message)

#几个常用的字符串方法
#len获得字符串长度，返回类型为int
s1 = "plagiaristic"
print(len(s1))
#isalnum判断字符串是否只包含数字或只包含字母，返回True或False
s2 = "github.com"
print(s2.isalnum())

#python中字符串的所有方法详见文档
#中文：https://docs.python.org/zh-cn/3/library/stdtypes.html#string-methods
#English version:https://docs.python.org/3/tutorial/introduction.html#strings


