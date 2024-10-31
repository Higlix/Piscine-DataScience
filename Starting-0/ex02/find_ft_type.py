def all_thing_is_obj(object: any) -> int:
#your code here
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String",
    }
    object_type = type_names.get(type(object))
    
    if object_type == None:
        print("Type Not Found")
    elif object_type == "String":
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print(str(object_type) + " : " + str(type(object))) 
    return 42