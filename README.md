# IDS_Responsive-system

Overview
This repository contains code and data files for an Intrusion Detection System project. The project involves data preprocessing, model training, and evaluation for intrusion detection.

Files
Jupyter Notebooks
1_preprocessing_file.ipynb

This Jupyter notebook contains the code for data preprocessing. It covers the following tasks:

Data Loading: Loading the raw intrusion detection dataset (Intrusion_data.csv).

Data Cleaning: Handling missing values and ensuring data consistency.

Data Visualization: Visualizing data distributions and patterns to gain insights.

Feature Engineering: Preparing the data for machine learning, including categorical encoding and resampling.

2_model_training_file.ipynb

This Jupyter notebook contains the code for model training and evaluation. It includes the implementation of two machine learning models:

Support Vector Classifier (SVC): Training and evaluation of an SVC model for intrusion detection.

Convolutional Long Short-Term Memory (LSTM) Model: Training and evaluation of a deep learning model for intrusion detection using Conv1D, LSTM, and other layers.

CSV Files
(Intrusion_data.csv)
This CSV file contains the raw dataset used in the project. It serves as the input data for data preprocessing and model training. The dataset likely includes various features related to network traffic and intrusion labels.
X_train.csv

This CSV file contains the training data used to train machine learning models. It includes preprocessed feature data for training, which may include scaled and resampled data.
X_test.csv

This CSV file contains the testing data used to evaluate machine learning models. It includes preprocessed feature data for testing, similar to X_train.csv.
y_train.csv

This CSV file contains the training labels corresponding to the X_train.csv data. It is used for model training and includes the target variable (intrusion labels).
y_test.csv 1.This CSV file contains the testing labels corresponding to the X_test.csv data. It is used for evaluating model performance and includes the target variable for testing data.

Usage
Clone this repository to your local machine.
Open the Jupyter notebooks for data preprocessing and model training.
Explore, modify, or run the code as needed.
The CSV files contain the data used in the notebooks.
Author
Vipul Tiwari

Feel free to explore the notebooks and data files. If you have any questions or suggestions, please open an issue.
