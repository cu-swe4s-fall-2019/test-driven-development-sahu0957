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
    pass

def combo(L, out_file_name):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description="returns specified column from stdin")
    parser.add_argument("out_file",
                        help="output PNG file",
                        type=str)
    parser.add_argument("out_type",
                        help="output PNG type",
                        type=str)
    args = parser.parse_args()
    X = []
    for l in sys.stdin:
        A = l.rstrip().split()
        X.append(float(A[col_num]))

    if out_type == 'histogram':
        pass
    if out_type == 'boxplot':
        pass
    if out_type == 'combo':
        pass


