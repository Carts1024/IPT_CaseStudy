mylist = []

mylist.append(67)
mylist.append(62.9)
mylist.append("hi")
mylist.append(False)

mylist = mylist + [8]
mylist = mylist + [67]
mylist = mylist + ["apple"]
mylist = mylist + [6.5]

mylist.append("banana")
mylist.append(67)
mylist.insert(2,"dog")
print(mylist)
mylist.insert(0,909)
print(mylist)
print(mylist.index("hi"))
print(mylist.count(67))
mylist.remove(67)
mylist.pop(5)
print(mylist)
