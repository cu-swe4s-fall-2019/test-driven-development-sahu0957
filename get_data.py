import sys
import argparse
import select

def read_stdin_col(col_num):
    # Only move forward with the script if stdin is empty
    # otherwise, exit to avoid the program stalling
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        X = []
        for l in sys.stdin:
            try:
                A = l.rstrip().split()
                X.append(float(A[col_num]))
            except IndexError:
                # Indexes specified that are out of range
                # will throw an error
                raise IndexError('Column does not exist!')
                sys.stderr.write('Column does not exist!')
                sys.exit(1)
        if len(X) == 0:
            # Lists of length 0 will return None, to avoid
            # errors in other scripts
            return None
        else:
            return X
    else:
        sys.stderr.write('No input data')
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description="returns specified column from stdin")
    parser.add_argument("column_index",
                        help="column index of stdin",
                        type=int)
    args = parser.parse_args()
    a = read_stdin_col(args.column_index)
    print(a)
