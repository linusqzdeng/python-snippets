import re

s = 'im linus, who are you?'

r = re.search('im(.*)\?', s)
print(r.group(1))