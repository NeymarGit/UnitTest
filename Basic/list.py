list = [1, 'x', "stringbuffer", [1, 2, 3], False]
print(len(list))

# 追加，一次只能添加一个元素
list.append("bb")
print(list)

# 插入元素
list.insert(2, 'lyh')
print(list)

# 删除元素,pop传索引值，返回删除了的元素
result = list.pop(2);
print("删除了：" + result)
print(list)
list.remove('x')
print(list)

# 修改
list[0] = "haha"
print(list)


# 元祖，不能删除修改,一般用于数据库
a = ('12')
print(type(a))
b = ('string')
print(type(b))


# 字典 无序的
a = {"score": "98.50", "age": 17, "name": "lyh"}
print(a['score'])
print(a.keys())
print(a.values())

# 删除,返回删除了的值value
result = a.pop("age")
print(result)
print(a)

# 新增
a["class"] = "1202"
print(a)

# 修改
a["class"] = "1201"
print(a)

