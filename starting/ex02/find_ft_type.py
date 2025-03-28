def all_thing_is_obj(object: any) -> int:
    type_map = {
        list: "List",
        dict: "Dict",
        tuple: "Tuple",
        set: "Set",
        str: "is in the kitchen",
    }
    obj_type = type(object)
    if obj_type in type_map:
        if (obj_type == str):
            print(f"{object} {type_map[str]} : {obj_type}")
        else:
            print(f"{type_map[obj_type]} : {obj_type}")
    else:
        print("Type not found")
    return 42
