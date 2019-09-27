import sys
import math_lib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Generate a boxplot from an input list
def boxplot(L, out_file_name):
    # Empty files will be handled by returning None, to avoid
    # any errors in processing
    if len(L) == 0:
        return None
    try:
        width = 3
        height = 3
        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.boxplot(L)
        mean = math_lib.list_mean(L)
        stdev = math_lib.list_stdev(L)
        label = 'mean:' + str(mean) + 'stdev:' + str(stdev)
        # List mean and standard deviation near the top of the plot
        plt.text(0.5, 35, label , fontsize=9) 
        plt.savefig(out_file_name, bbox_inches='tight')
    except TypeError:
        # Nonnumber entries will cause an error
        raise TypeError('List contains nonnumber entries!')


def histogram(L, out_file_name):
    # Empty files will be handled by returning None, to avoid
    # any additional errors
    if len(L) == 0:
        return None
    width = 3
    height = 3
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    label = 'mean:' + str(mean) + 'stdev:' + str(stdev)
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(L, 5)
    plt.text(0.5, 32, label , fontsize=9) 
    plt.savefig(out_file_name, bbox_inches='tight')
    # Nonnumber entries are allowed for histogram generation

def combo(L, out_file_name):
    # Empty files will be handled by returning None, to avoid
    # any additional errors
    if len(L) == 0:
        return None
    try:
        width = 5
        height = 3
        mean = math_lib.list_mean(L)
        stdev = math_lib.list_stdev(L)
        label = 'mean:' + str(mean) + 'stdev:' + str(stdev)
        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(1, 2, 1)
        ax.boxplot(L)
        ax = fig.add_subplot(1, 2, 2)
        ax.hist(L, 5)
        plt.text(0, 25, label , fontsize=9) 
        plt.savefig(out_file_name, bbox_inches='tight')
    except TypeError:
        # Boxplots can't handle nonnumber entries, so
        # this will throw an error
        raise TypeError('Nonnumber entries in list!')
