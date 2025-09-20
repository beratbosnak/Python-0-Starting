def all_thing_is_obj(object: any) -> int:
    """
    Prints the type of the object based on specific rules
    and always returns 42.
    """

    if type(object) is list:
        print("List :")
    elif type(object) is tuple:
        print("Tuple :")
    elif type(object) is set:
        print("Set :")
    elif type(object) is dict:
        print("Dict :")
    elif type(object) is str:
        print(f"{object} is in the kitchen :")
    else:
        print("Type not found")
    return 42
