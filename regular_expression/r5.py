import re

s = 'ABCFDOIJEalsknfe1398345'

r = re.match('\D', s)
print(r.span())
