# OLA2-Supervised Learning Assignment

This repository contains the work for the "OLA2-Supervised Learning" assignment, created by **Jamie, Helena, and Isak.**

## Files in the Repository

**[`PredictionScript.py`](https://github.com/TofuBytes-Studies-Group/OLA2_ML_AI/blob/main/PredictionScript.py)**: This Python script is the core of our housing price prediction application. It allows users to select between three different models (Linear Regression, Random Forest, and XGBoost) to predict the price of a house based on various features. 

**[`OLA2_Housing_Prediction.ipynb`](https://github.com/TofuBytes-Studies-Group/OLA2_ML_AI/blob/main/OLA2_Housing_Prediction.ipynb)**: This Jupyter notebook contains the exploratory data analysis (EDA), preprocessing steps, model training, and evaluation process for our housing price prediction project. It also provides the code for training the three models mentioned above and exporting them as `.pkl` files.

**[`Presentation.pdf`](https://github.com/TofuBytes-Studies-Group/OLA2_ML_AI/blob/main/Presentation.pdf)**: This PDF file contains our short presentation on the explanation of measuring distance between
data points using Manhattan, Euclidean and Hamming distance also 
- Also a link to the google slides presentation if view of the presentation notes is of interest, as a presentation is not supposed to have long monoliths of texts(see what i did there?), as it intereferes severely with user concentration: [Google Slides Link](https://docs.google.com/presentation/d/1ed3Tt9Gjt17G0c_IcVNlqk5WO07NRovDat30zzedOx8/edit?usp=sharing)

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
