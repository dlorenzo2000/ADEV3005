# Date: Tue Jan03/23
# Created by: Dean Lorenzo
# Purpose: Challenge p.67 from text

phrase = ("Don't panic")
plist = list(phrase)
print(phrase)
print(plist)

for i in range(3):
    plist.pop()
plist.pop(0)

plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))


new_phrase = (''.join(plist))
print(phrase)
print(plist)
print(new_phrase)