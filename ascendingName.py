# -*- coding:utf-8 -*-
import json
import os

"""
这是一般软件（wps）pdf 转图片后的格式
我json_encode 后 放在数据库
"""


name = input('请输入名字：')
page = int(input('请输入页数：'))

n = 0
lists = []
pre = '/images/gb/name/'
while int(n) <= page:
    lists.append(pre + name + str(n).zfill(2) + '.jpg')
    n += 1

result = json.dumps(lists)
os.system("echo '%s' | pbcopy" % result)
print(lists)
print('已经输出到剪贴板')
