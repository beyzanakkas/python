def rvr(nlist):
    """
    Reverse the nested lists
    """
    nlist.reverse()
    for i in nlist:
        if type(i) is list:
            rvr(i)    
