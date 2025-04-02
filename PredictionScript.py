import joblib
import pandas as pd

def load_model(model_name):
    """Loads a model from a given filename."""
    model = joblib.load(model_name)
    return model

def get_user_choice():
    """Provides a console-based selection for the model."""
    print("\nSelect a model for prediction:")
    print("1. Linear Regression (LR)")
    print("2. Random Forest (RF)")
    print("3. XGBoost (XGB)")
    print("4. Exit")
    
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        return "LR_model.pkl"
    elif choice == "2":
        return "RF_model.pkl"
    elif choice == "3":
        return "tuned_XGB_model.pkl"
    elif choice == "4":
        return None  # Exit the loop
    else:
        print("Invalid choice, defaulting to Linear Regression.")
        return "LR_model.pkl"

def make_prediction(model, features):
    """Make a prediction using the selected model."""
    feature_values = [
        features["area"],
        features["bedrooms"],
        features["bathrooms"],
        features["stories"],
        features["parking"],
        features["mainroad_yes"],
        features["guestroom_yes"],
        features["basement_yes"],
        features["hotwaterheating_yes"],
        features["airconditioning_yes"],
        features["prefarea_yes"],
        features["furnishingstatus_semi-furnished"],
        features["furnishingstatus_unfurnished"]
    ]
    
    # Create a DataFrame to match the model's expected input structure
    feature_df = pd.DataFrame([feature_values], columns=[
        'area', 'bedrooms', 'bathrooms', 'stories', 'parking', 'mainroad_yes', 
        'guestroom_yes', 'basement_yes', 'hotwaterheating_yes', 'airconditioning_yes',
        'prefarea_yes', 'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished'
    ])
    
    # Use the model to make the prediction
    prediction = model.predict(feature_df)
    return prediction[0]  # Return the predicted price

def get_default_features():
    """Provide default feature values for the user."""
    print("\nHere are the default values you can use to get a prediction:")
    print("area = 7420, bedrooms = 4, bathrooms = 2, stories = 3, parking = 2")
    print("mainroad = yes, guestroom = no, basement = no, hotwaterheating = yes, airconditioning = yes")
    print("prefarea = yes, furnishingstatus = furnished")
    return {
        "area": 7420,
        "bedrooms": 4,
        "bathrooms": 2,
        "stories": 3,
        "parking": 2,
        "mainroad_yes": True,
        "guestroom_yes": False,
        "basement_yes": False,
        "hotwaterheating_yes": True,
        "airconditioning_yes": True,
        "prefarea_yes": True,
        "furnishingstatus_semi-furnished": False,
        "furnishingstatus_unfurnished": False
    }

def main():
    while True:
        model_file = get_user_choice()
        if model_file is None:
            print("Exiting program.")
            break  # Exit the loop if the user chooses to exit
        
        # Load the selected model
        selected_model = load_model(model_file)
        print(f"Loaded model: {model_file}")
        
        # Get features from user or use defaults
        use_default = input("Would you like to use the default feature values? (y/n): ").lower()
        if use_default == "y":
            features = get_default_features()
        else:
            features = {}
            features["area"] = float(input("Enter area: "))
            features["bedrooms"] = int(input("Enter number of bedrooms: "))
            features["bathrooms"] = int(input("Enter number of bathrooms: "))
            features["stories"] = int(input("Enter number of stories: "))
            features["parking"] = int(input("Enter number of parking spaces: "))
            features["mainroad_yes"] = input("Is there a main road nearby? (yes/no): ").lower() == "yes"
            features["guestroom_yes"] = input("Is there a guestroom? (yes/no): ").lower() == "yes"
            features["basement_yes"] = input("Does it have a basement? (yes/no): ").lower() == "yes"
            features["hotwaterheating_yes"] = input("Does it have hot water heating? (yes/no): ").lower() == "yes"
            features["airconditioning_yes"] = input("Does it have air conditioning? (yes/no): ").lower() == "yes"
            features["prefarea_yes"] = input("Is it in a preferred area? (yes/no): ").lower() == "yes"
            features["furnishingstatus_semi-furnished"] = input("Is it semi-furnished? (yes/no): ").lower() == "yes"
            features["furnishingstatus_unfurnished"] = input("Is it unfurnished? (yes/no): ").lower() == "yes"

        # Make prediction
        predicted_price = make_prediction(selected_model, features)
        print(f"Predicted House Price: {predicted_price}")

if __name__ == "__main__":
    main()
