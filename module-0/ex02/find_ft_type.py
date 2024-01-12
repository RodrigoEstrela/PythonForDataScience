def all_thing_is_obj(obj: any) -> int:
    if isinstance(obj, list):
        print("List : {}".format(type(obj)))
    elif isinstance(obj, tuple):
        print("Tuple : {}".format(type(obj)))
    elif isinstance(obj, set):
        print("Set : {}".format(type(obj)))
    elif isinstance(obj, dict):
        print("Dict : {}".format(type(obj)))
    elif isinstance(obj, str):
        print("{} is in the kitchen : {}".format(obj, type(obj)))
    else:
        print("Type not found")

    return 42

