def NULL_not_found(object: any) -> int:
    NULL_map = {
        "None"    	: "Nothing: None"	,
        "0"       	: "Zero: 0"			,
        ''      	: "Empty:"			,
        "nan"		: "Cheese: nan"		,
        "False" 	: "Fake: False"		,
    }
    string = str(object)
    obj_type = type(object)
    if  string in NULL_map:
        print(f"{NULL_map[string]} {obj_type}")
        return 0
    else :
        print("Type not found")
    return 1

"""

For this exercise, I tried the same approach as in the previous exercise, 
but it didn't work because each type in {None, 0, '', nan, False} has a special format
that prevents the Python interpreter from handling them as expected.
So, I tried something different: I converted everything to a string, and it worked.

The point is, these types are not like other types that can be used automatically by their literal value, you need to convert them.
"""
