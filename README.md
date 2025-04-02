# OLA2-Supervised Learning Assignment

This repository contains the work for the "OLA2-Supervised Learning" assignment, created by Jamie, **Helena, and Isak.**

## Files in the Repository

- **`PredictionScript.py`**: This Python script is the core of our housing price prediction application. It allows users to select between three different models (Linear Regression, Random Forest, and XGBoost) to predict the price of a house based on various features.
  
  To run the application, make sure the required models (`LR_model.pkl`, `RF_model.pkl`, `tuned_XGB_model.pkl`) are in the same directory as the script. You can execute it via the command line, and it will guide you through selecting a model and entering feature values.

- **`OLA2_Housing_Prediction.ipynb`**: This Jupyter notebook contains the exploratory data analysis (EDA), preprocessing steps, model training, and evaluation process for our housing price prediction project. It also provides the code for training the three models mentioned above and exporting them as `.pkl` files.

- **`Presentation.pdf`**: This PDF file contains our final presentation for the assignment, detailing our approach, methodology, and results of the housing price prediction model.

## How to Run the Prediction Script

1. Make sure you have the necessary Python packages installed. You can install them using the following:

   ```bash
   pip install numpy
   pip install pandas
   pip install scikit-learn==1.5.1
   pip install xgboost

2. Run the script using the following command:
    ```bash
    python PredictionScript.py

## How to Use the Jupyter Notebook
Open the OLA2_Housing_Prediction.ipynb file in Jupyter Notebook.

**Execute each cell sequentially to perform the EDA, preprocess the data, train the models, and give out results**
- `BE AWARE THAT THE XGBOOST MODEL TAKES APROX. 2 MINUTES TO COMPLETE`