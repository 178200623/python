# -*- coding: UTF-8 -*-
#笨办法学编程py3-读取文件

from sys import argv

script, filename = argv

text = open(filename)
print("Here's your file %r " % filename)

print (text.read())
text.close()

print("Type the filename again:")

file_again = input(" > ")

text_again = open(file_again)
print(text_again.read())
text_again.close()
