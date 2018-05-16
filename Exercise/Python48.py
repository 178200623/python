#-*- coding:UTF-8 -*-
#笨办法学编程py3---异常,扫描
def cover_number(s) :
    try:
        print("this function's value:", s)
        return int(s)
    except ValueError:
        return None
'''
a = cover_number('python')
print(a)
b = cover_number(12305)
print(b)
'''


stuff = input("> ")
print("input value:",stuff)
words = stuff.split()
print("split value:",words)



#sentence.scan(words)

