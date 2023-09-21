# Introduction To The Notebooks Of A Capstone Project 

![tom_superstore](images/1_tom_stuperstore.png)

This repository contains the Jupyter Notebooks of a capstone project carried out within the framework of a boot camp of *neuefische* executed during summer 2023. This project is based on a [kaggle challenge provided by Walmart Recruiting](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/overview) and aims to predict the weekly sales of different supermarket stores all over the country.

In order to successfully run the Jupyter Notebooks, please download the original data files from [Kaggle](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data) and save it to ```./data/"```

Our notebooks follow the Data Science Lifecycle: from wrangling and  cleaning to EDA, than feature engineering to the model and its error analysis. Since the notebooks build on each other, we ask that you run them in the correct order. This will provide the correct files for the models. 
For example, for the best model Extra Trees (06.1), please run Notebook 01, 02 and 05.1 locally. To run EDA (03) or the baseline model (04) you just need to run 01 and 02 before.

Please also set up a new virtual environment. For this purpose use the following commands:

```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements_dev.txt
```

The added [requirements file](requirements.txt) contains all libraries and dependencies to properly execute the code. 

This repo's folder Notebooks contains within notebooks following chapters:

- [01 Data Wranging](Notebooks/01_dataframe_merging.ipynb)
- [02 Data Cleaning](Notebooks/02_data_cleaning.ipynb)
- [03 Exploratory data analysis](Notebooks/03_eda.ipynb)
- [04 Baseline model](Notebooks/04_baseline_model.ipynb)
- [05.1 Feature Engineering ExtraTrees](Notebooks/05.1_feature_engineering_extratrees.ipynb)
- [05.2 Feature Engineering Random Forest](Notebooks/05.2_feature_engineering_randomforest.ipynb)
- [06.1 Modelling Extra Trees](Notebooks/06.1_best_model_extratrees.ipynb)
- [06.2 Modelling RandomForest](Notebooks/05.2_feature_engineering_randomforest.ipynb)
- [06.3 Modelling KNN](06.3_modelling_knn.ipynb)
- [07 Plotting for presentation](Notebooks/07_plots_presentation.ipynb)
