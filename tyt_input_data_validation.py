def data_keys_are_valid(data_dict:dict, keys:list)->bool:
    return ['csrfmiddlewaretoken']+keys==list(data_dict.keys())
