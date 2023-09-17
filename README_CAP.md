# Introduction To The Notebooks Of A Capstone Project 

![Supermarket](./images/4_supermarket_hanson-lu-sq5P00L7lXc-unsplash.jpg)

Photo by <a href="https://unsplash.com/@hansonluu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Hanson Lu</a> on <a href="https://unsplash.com/photos/sq5P00L7lXc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
This repository contains the Jupyter Notebooks of a capstone project carried out within the framework of a boot camp of 'neue fische' executed during summer 2023. This project is based on a ["kaggle challenge" provided by Walmart Recruiting](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/overview) and aims to predict the weekly sales of different supermarket stores all over the country.
In order to successfully run the Jupyter Notebooks, please download the original data files from [Kaggle](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data) and save it to ```./data/"```

Please also set up a new virtual environment. For this purpose use the following commands:

```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

The added [requirements file](requirements.txt) contains all libraries and dependencies to properly execute the code. 

This repo contains following chapters:

### TO BE UPDATED LATER
- [01 Data Exploration](01_data_exploration.ipynb)
- [02 Data Cleaning](02_data_cleaning.ipynb)
- [03 Exploratory data analysis](03_eda.ipynb)
- [04 Base line model](04_Baselinemodel.ipynb)
- [05 Feature Engineering](05_feature_engineering.ipynb)
- [06 Modelling](06_modelling.ipynb)
- [07 Hyperparameter Tuning](07_Hyperparameter_Tuning.ipynb)
- [08 Modelling with best Hyperparameter](08_Modeling_with_best_hyperparams.ipynb)
- [09 Plotting results](09_Plotting_results.ipynb)