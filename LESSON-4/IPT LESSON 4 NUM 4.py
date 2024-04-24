mylist = []

num_list = int(input("How many elements do you want in the list?: "))
sum = 0
for _ in range(num_list):
    element = int(input("Enter an element: "))
    sum = sum + element
    mylist.append(element)
    

print(sum)
print(mylist[-1])
mylist.reverse()
print(mylist)
if 5 in mylist:
    print('Yes')
else:
    print('No')
element_count = 0
for _ in mylist: 
    if _ < 5:
        element_count += 1
        

print(element_count)
mylist.pop(0)
mylist.pop(-1)
mylist.sort()
print(mylist)

