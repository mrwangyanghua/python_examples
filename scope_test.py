#!/usr/bin/python
# -*- coding:utf-8 -*-

def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam  = "global spam"


    spam = "test spam"
    do_local()
    print("After local assigments: {0}".format(spam))
    do_nonlocal()
    print("After nonlocal assigments: ", spam)
    do_global()
    print("After global assigments: ", spam)


scope_test()
print("In glboal scope:", spam)
