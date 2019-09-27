test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

# Test whether we get the expected output file, run for each module
bash gen_data.sh | python viz.py --out_file test.png --plot_type histogram
A=`ls test.png`
run test_file_gen_histogram echo $A
assert_in_stdout 'test.png'
[ -e test.png ] && rm test.png

bash gen_data.sh | python viz.py --out_file test.png --plot_type boxplot
A=`ls test.png`
run test_file_gen_boxplot echo $A
assert_in_stdout 'test.png'
[ -e test.png ] && rm test.png

bash gen_data.sh | python viz.py --out_file test.png --plot_type combo
A=`ls test.png`
run test_file_gen_combo echo $A
assert_in_stdout 'test.png'
[ -e test.png ] && rm test.png

# Test whether we exit when we specify a bad parameter
run test_bad_params bash gen_data.sh | python viz.py --out_file test.png --plot_type foo
# Python isn't writing to bash stderr, so I call exit codes from $? instead
A=`echo $?`
assert_equal $A 1


