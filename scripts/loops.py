#!/bin/python3

def for_loop(size=1):#not an actual for loop rather, a for-each loop
    li=[]
    for i in range(size):
        li.append(i)

    return [i for i in range(10)]

def while_loop(size=1):#standard while loop
    li=[]
    i = 0

    while i < size:
        li.append(i)
        i += 1
    return li

def main():
    string = list("abcd")
    list_a = for_loop()
    list_b = while_loop()
    list_c = string.reverse()
    print(string)
    print(list_c)
if __name__ == '__main__':
    main()
