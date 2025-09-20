def NULL_not_found(object: any) -> int:
    """
    Prints the object and its type for various "null" or "falsy" values.
    Returns 0 for handled types, 1 for unhandled types.
    """
    obj_type = type(object)

    if object is None:
        print(f"Nothing: {object} {obj_type}")
        return 0
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {obj_type}")
        return 0
    elif object is False:
        print(f"Fake: {object} {obj_type}")
        return 0
    elif object == 0 and not isinstance(object, bool):
        print(f"Zero: {object} {obj_type}")
        return 0
    elif object == '':
        print(f"Empty: {obj_type}")
        return 0
    else:
        print("Type not Found")
        return 1
