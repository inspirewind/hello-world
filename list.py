element = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O']

'''
print(element)
print(element[0])
print(element[-1])
'''

'''
print(element)
element.pop() #会更改删除原有列表中的元素
print(element)
'''

#切片slice
#当想取用列表中一部分元素时，可以使用切片

print(element[0:3])
#从0开始取，到3结束，不包括3，即左闭右开原则（虽然在语法表示上两边都是闭区间）

#利用切片特性可以简化代码
'''
#取出list前三个元素，用这三个元素组成新列表
a = []
for i in range(3):
	a.append(element[i])
print(a)
#等价于
a = element[0:3]
print(a)
'''

#切片的详细特性，参见文档：https://docs.python.org/zh-cn/3/tutorial/introduction.html#lists
#应用切片时，始终注意切片返回一个列表




#advanced syntax: list表达式
#一般形式 [expression1 for x in range(a,b) if expression2 for i in range(c,d) if expression3 ]
#等价于
'''
for x in range(a,b)
	if expression2
		for y in range(c,d)
			if expression3
				expression1
'''

#从左向右依次嵌套了由外向内的多个循环，第一的for循环前面的表达式是最内层的语句

'''
#应用:构造列表
#已知数组a和整数x，新建一个数组b，使b中包含a中所有小于x的元素
a = [5, 32, 63, 40, 93, 58, 22, 43, 90, 8, 31]
x = 50
b = [i for i in a if i < x] #注意for循环前面的i
print(b)
'''