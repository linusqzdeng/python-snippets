import re

me = 'Linus, linUs, LINUS'

r = re.findall('linus.', me, re.I)
print(r)
