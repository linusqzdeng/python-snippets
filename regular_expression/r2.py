# 字符集
import re

x = 'abc, acc, afc, adc, agg'
r = re.findall('a[^cfb]c',x)

print(r)
