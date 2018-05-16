#-*- coding:UTF-8 -*-
#笨办法学编程py3---循环和列表 for

hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count :
    print("Yhis is count %d " % number)

for fruit in fruits :
    print("A fruit of type: %s " % fruit)

for i in change :
    print("I got %r" % i)

elements = []

for i in range(0,6) :
    print("Adding %d to the list ." % i)
    elements.append(i)
for i in range(6,0,-1) :
    print("Adding %d to the list ." % i)
    elements.append(i)

print(elements)
for i in elements :
    print("Elements was : %d " % i)