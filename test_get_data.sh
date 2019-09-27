test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

# Test whether we exit when no stdin is there
run read_no_stdin python get_data.py 0
assert_exit_code 1

# Test whether we exit when we specify a bad index value
run read_badindex bash gen_data.sh | python get_data.py 0
assert_exit_code 1

# Test whether we have the right columns
A=`printf "1\t5\n2\t6" | python get_data.py 0`
run read_stdin echo $A
assert_in_stdout '[1.0, 2.0]'
