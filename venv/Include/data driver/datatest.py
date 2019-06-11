# coding=utf-8
from xml.dom import minidom

# 打开xml文件
date = minidom.parse('info.xml')

# 得到文档的对象
root = date.documentElement

# 获取标签名为province的一组标签
provinces = root.getElementsByTagName('province')
citys = root.getElementsByTagName('city')

# 获取第二个province标签对的值，firstChild返回被选节点的第一个子节点，data表示获取该节点的数据
p2 = provinces[1].firstChild.data
print(p2)

# 获取第一个city标签对的值
c1 = citys[0].firstChild.data
print(c1)

# 获取第二个city标签对的值
c2 = citys[1].firstChild.data
print(c2)


