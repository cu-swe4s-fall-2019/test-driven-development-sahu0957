import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def boxplot(L, out_file_name):
    if len(L) == 0:
        return None
    try:
        width = 3
        height = 3
        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(1,1,1)
        ax.boxplot(L)
        plt.savefig(out_file_name,bbox_inches='tight')
    except TypeError:
        raise TypeError('List contains nonnumber entries!')
    except:
        print("An unknown exception has occured. Exiting...")
        sys.exit(1)

def histogram(L, out_file_name):
    if len(L) == 0:
        return None
    try:
        width = 3
        height = 3
        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(1,1,1)
        ax.hist(L, 5)
        plt.savefig(out_file_name,bbox_inches='tight')
    except:
        print("An unknown exception has occured. Exiting...")
        sys.exit(1)

def combo(L, out_file_name):
    if len(L) == 0:
        return None
    try:
        width = 5
        height = 3
        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(1, 2, 1)
        ax.boxplot(L)
        ax = fig.add_subplot(1, 2, 2)
        ax.hist(L, 5)
        plt.savefig(out_file_name,bbox_inches='tight')
    except TypeError:
        raise TypeError('Nonnumber entries in list!')
    except:
        print("An unknown exception has occured. Exiting...")
        sys.exit(1)
