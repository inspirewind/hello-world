element = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']

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

#advanced syntax: 列表推导式
#一般形式 [expression1 for x in range(a,b) if expression2 for i in range(c,d) if expression ]
#等价于
'''
for x in range(a,b)
	if expression2
		for y in range(c,d)
			if expression3
				expression1
'''

#从左向右依次嵌套了由外向内的多个循环，第一的for循环前面的表达式是最内层的语句

#应用:构造列表
#已知数组a和整数x，新建一个数组b，使b中包含a中所有小于x的元素
a = [5, 32, 63, 40, 93, 58, 22, 43, 90, 8, 31]
x = 50
b = [i for i in a[1:] if i < x] #注意for循环前面的i
print(b)