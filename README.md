# House_prices-prediction

### Problem Statement
Help Alzar, the record keeper for finding lost details of 3.5k houses with the help of Machine Learning.

### Installation
* Clone repository and run **dataset_creation.py** and then **train_test_files_creation.py** to create dataset.
  * Dataset is given in form of text files so preprocessing is required to convert them into `csv file`
  * Firstly `dataset_creation.py` extracts data from text files and make `finaldataset.csv`.
  * Then `train_test_files_creation.py` uses pandas library to split finaldataset.csv into testing and training dataset on basis of house prices.

### Requirements
* This problem statement uses **xgboost Regressor** so it must be installed through either of these ways.
  * **Using pip-** `pip install xgboost`
  * **Using conda-** `conda install -c py-xgboost`
* Python2.7 is preferred for this project.

### Usage
* Run `dataset_creation.py` followed by `train_test_files_creation.py` to create and split dataset from raw text files to processed csv files.
* Run `features_analysis.py`  to visualize train and test dataset using functions of pandas dataframe. It helps in visualizing relations between features and target value with the help of **histogram, scatter plots** and  **Heat Map**.

![Heat Map](https://github.com/pintugawar/House-Prices-Predictions/blob/master/Screenshot%20from%202018-07-09%2018-05-18.png)

* Run `algo.py` for trying new features and feature selection and filling **NaN** values through **interpolation**.
  * After this data is ready to fit for different models.
  * This gives detail `time` and `r2_score analysis` after tuning hyperparameters of different types of regressions.
  * This will run `cross validation` across the training set on **LinearRegression**, **LassoRegression**, **Ridge Regression** which prints `r2_score`.


### Results
* Finally run `final_solution_xgboost.py` to get the final results
* With the help of `xgboost regressor` we are able to achieve r2_score of **0.99512**.
* `solution.csv` is also given in repository to match results of test dataset.
* xgboost with tuned parameters gives final `r2_score` of **0.99553** on test dataset.

