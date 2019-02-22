
#this is a single line comment

'''
This is a multi-line comment,
we don't have a concern for newlines here ;)
'''

a = 1   # I'm a standard sized integer
b = 3.0 #I'm a standard sized float
c = 10 ** 24 #I'm a long integer

a_string = "I'm a string!"
im_a_boolean = True

an_allowed_variable_name = "Me"
_also_allowed = "Moi"
#9_not_allowed = "Yo"
#if you get this one, congrats ____
#&_allowed_but_discouraged = "washi"

def some_function():
    a = 10
    print("I'm a local variable : {}".format(a))
    return

def list_stuff():
    im_a_list = list("IM A LIST".split())
    im_also_a_list = ["a",5,'hello',3.5]

    print(im_a_list)
    print(im_also_a_list)
    return

if __name__ =='__main__':
    list_stuff()
