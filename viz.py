import argparse
import data_viz
import get_data
import math_lib
import sys

def main():
    # Handle input arguments
    parser = argparse.ArgumentParser(
    description="calculate mean and std. dev of an input list")
    parser.add_argument("--out_file", help="output file name", type=str)
    parser.add_argument('--plot_type', help="boxplot, histogram or combo plot output \
                        (default: combo)", default = "combo")
    args = parser.parse_args()
    
    # Determine which plot is specified
    if args.plot_type == 'boxplot':
        L = get_data.read_stdin_col(0)
        data_viz.boxplot(L, args.out_file)
    elif args.plot_type == 'histogram':
        L = get_data.read_stdin_col(0)
        data_viz.histogram(L, args.out_file)
    elif args.plot_type == 'combo':
        L = get_data.read_stdin_col(0)
        data_viz.combo(L, args.out_file)
    else:
        # If no recognized plot is specified, return an error
        sys.stderr.write('Unrecognized plot type!')
        sys.exit(1)

if __name__ == '__main__':
    main()
