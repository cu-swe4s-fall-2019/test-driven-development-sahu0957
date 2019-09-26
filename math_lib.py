import sys
import math
import argparse


def list_mean(L):
    if L is None:
        return None
    if len(L) == 0:
        return None

    s = 0

    for l in L:
        try:
            s += l
        except TypeError:
            raise TypeError('Detected nonnumber value in list! Exiting...')
    return(s/len(L))


def list_stdev(L):
    if L is None:
        return None
    if len(L) == 0:
        return None
    else:
        mean = list_mean(L)
        if len(L) == 1:
            raise ZeroDivisionError("Can't calculate stdev on single \
                                    entry! Exiting...")
        stdev = math.sqrt(sum([(mean-x)**2 for x in L]) / (len(L) - 1))
        return stdev


if __name__ == '__main__':
    # Read input arguments, if the function is called as the main
    parser = argparse.ArgumentParser(
        description="calculate mean and std. dev of an input list")

    parser.add_argument("numeric_list", help="input list", type=list)
    args = parser.parse_args()
    input_list = [float(i) for i in args.numeric_list]
    r = list_mean(input_list)
    p = list_stdev(input_list)
    print('list mean:', r)
    print('list standard deviation:', p)
