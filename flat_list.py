def flatten_list(l):
    """
    Generate a flatten list from the input list
    """
    flat_list = []
    for i in l:
        if type(i) is list:
            flat_list += flatten_list(i)
        else:
            flat_list.append(i)
    return flat_list
