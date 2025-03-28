import sys

argc = len(sys.argv)
if argc > 2:
    print("AssertionError: more than one argument is provided")
if argc == 2:
    try:
        num = int(sys.argv[1])
        if (num % 2 == 1):
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except ValueError:
        print("AssertionError: argument is not an integer")


"""
In this exercise, we take a look at two new concepts.

The first concept is taking arguments from the user before running the program,
for which we use the sys module.

See this link for more information about the sys module:
https://peppered-mine-9af.notion.site/Sys-module-in-Python-1c44665ba38a8053a796fee1bf4307eb

The second concept is using try and except to check if the syntax works
correctly and to prevent the program from crashing when an error occurs.

See this link for more information about the try and except concept:
https://peppered-mine-9af.notion.site/Try-and-except-1c44665ba38a80709240d2ed78cd9823?pvs=73
"""
