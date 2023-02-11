def data_keys_are_valid(input_keys:list, keys:list)->bool:
    keys+=['csrfmiddlewaretoken']
    if len(keys)!=len(input_keys): return False
    for i in range(len(keys)):
        if keys[i] not in input_keys: return False
    return True  
