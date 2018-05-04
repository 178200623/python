# -*-coding: UTF-8 -*-
#笨办法学编程py3-更多的变量和打印

my_name = 'Zed A.Shaw'
name = "{}".format("Zed A.Shaw")

my_age = 35 #not a lie
age = "{}".format(35)

my_height = 74 #inches
height = "{:d}".format(74)

my_weight = 180 #lbs
weight = "{:d}".format(180)

my_eyes = 'Blue'

my_teeth = 'White'

my_hair = 'Brown'

print("Let's talk about %s." % my_name)

print("He's %d inches tall." % my_height)

print("He's %d pounds heavy." % my_weight)

print("Actually that's not too heavy")

print("He's got %s eyes and %s hair." % (my_eyes, my_hair))

print("His teeth are usually %s depending on the coffee." % my_teeth)

#this line is tricky ,try to get it exactly right

print("If I add %d,%d, and %d I get %d." %(my_age,my_height,my_weight,my_age + my_height + my_weight))

print("If I add {},{}, and {} I get {}.".format(age,height,weight,int(age) + int(height) + int(weight)))
