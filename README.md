# test-driven-dev
Test Driven Development

This package creates a histogram or boxplot, or a combo of both from an input list. Additionally, the plots will display both the mean and standard deviation of the distribution. These plots are displayed from matplotlib's plot generating libraries

## Installation
This program should be run in a conda environment. Install conda and its dependencies as follows:
```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels r
conda create --yes -n test
conda activate test
conda install -y pycodestyle
conda install --yes python=3.6
conda install matplotlib
```

## Running the Program
Pass a bash numbered array to viz.py to start the program. Included in the package is a script that randomly generates one such file. Specify whether you want a histogram, boxplot or a combo of both, and the file will be saved to the path specified by the --out_file flag:
```sh
bash gen_data.sh | python viz.py --out_file test.png --plot_type (histogram, boxplot, combo)
```

## Testing the Program
The files test_get_data.sh and test_viz.sh perform various functional tests on the two corresponding python scripts get_data.py and viz.py
```sh
bash test_get_data.sh
bash test_viz.sh
```

The file test_math_lib.py and test_data_viz.py will perform a suite of unit-tests on the individual modules found in their corresponding python scripts math_lib.py and data_viz.py

```python
python test_math_lib.py
python test_data_viz.py
```
Note that all of these tests are run in the .travis.yml CI before updating this repository on GitHub

## Release History
*1.0\
	*CHANGE: Updated get_data.py to receive a delimited numeric file, and return a specific column\
	*CHANGE: Updated data_viz.py to show boxplots, histograms, and combo plots specified by the user\
	*CHANGE: Updated math_lib.py to return means and standard deviations of lists input through stdin\
	*CHANGE: Updated viz.py to generate a user-specified plot type from data fed through stdin\
	*CHANGE: Updated .travis.yml file to automatically perform functional/unit testing before updating GitHub repository\
    	*ADDED: Functional and Unit testing scripts test_data_viz.py, test_math_lib.py, test_viz.sh, and test_get_data.sh to ensure that all scripts are working properly\

## To Contribute
1. Fork it (< https://github.com/cu-swe4s-fall-2019/best-practices-sahu0957.git>)
2. Create your feature branch (`git checkout -b feature_branch`)
3. Commit your changes (`git commit -m 'add your notes'`)
4. Push to the branch (`git push origin feature_branch`)
5. Create a new Pull request



