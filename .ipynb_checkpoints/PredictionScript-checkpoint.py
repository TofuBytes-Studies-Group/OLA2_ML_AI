import joblib
import numpy as np

def load_model(model_name):
    try:
        return joblib.load(model_name)
    except FileNotFoundError:
        print(f"Error: {model_name} not found.")
        return None

def get_user_input():
    try:
        features = input("Enter the features as comma-separated values: ")
        return np.array([list(map(float, features.split(',')))]).reshape(1, -1)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_user_input()

def main():
    models = {
        "1": "tuned_XGB_model.pkl",
        "2": "LR_model.pkl",
        "3": "RF_model.pkl"
    }
    
    print("Choose a model:")
    print("1 - XGBoost")
    print("2 - Linear Regression")
    print("3 - Random Forest")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice not in models:
        print("Invalid choice. Exiting.")
        return
    
    model = load_model(models[choice])
    if model is None:
        return
    
    features = get_user_input()
    prediction = model.predict(features)
    
    print(f"Predicted price: {prediction[0]}")

if __name__ == "__main__":
    main()
