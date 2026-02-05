"""
This is an example to demonstrate the function call stack in Python.
"""

def func_one():
    func_two()
    print("This is function one")

def func_two():
    func_three()
    print("This is function two")

def func_three():
    func_four()
    print("This is function three")

def func_four():
    print("This is function four")


func_four()
func_one()