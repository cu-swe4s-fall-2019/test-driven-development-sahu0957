
def list_mean(L):
    if L is None:
        return None
    if len(L) == 0:
        return None

    s = 0

    for l in L:
        s += l

    return(s/len(L))

def list_stdev(L):
    return None
