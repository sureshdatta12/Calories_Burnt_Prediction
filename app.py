import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pandas as pd
import numpy as np

# Load dataset from a CSV file
df = pd.read_csv(r'C:\Users\balas\Desktop\APPLICATION DEVELOPMENT-2\datasets\exercise.csv')
df2 = pd.read_csv(r'C:\Users\balas\Desktop\APPLICATION DEVELOPMENT-2\datasets\calories.csv')
calories_data = pd.concat([df,df2['Calories']], axis=1)
calories_data.replace({"Gender":{'male':0,'female':1}},inplace=True)

# Assuming 'X' contains the feature columns and 'y' contains the target variable
X = calories_data.drop(columns=['User_ID','Calories'],axis=1)
y = calories_data['Calories']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=10)

# Train an XGBoost regressor
model = XGBRegressor()
model.fit(X_train, y_train)

# Tkinter GUI
root = tk.Tk()
root.title("Calories Burnt Prediction (XGBoost)")

# Function to predict calories burnt
def predict_calories():
    try:
        # Get user input from GUI
        duration = float(entry_duration.get())
        heart_rate = float(entry_heart_rate.get())
        age = int(entry_age.get())
        weight = float(entry_weight.get())
        body_temperature = float(entry_body_temperature.get())

        # Make a prediction using the trained model
        prediction = model.predict(X_test)

        # Display the prediction
        messagebox.showinfo("Prediction", f"Predicted Calories Burnt: {prediction[0]:.2f} calories")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# GUI components
label_duration = Label(root, text="Duration (minutes):")
label_duration.grid(row=0, column=0, padx=10, pady=10)
entry_duration = Entry(root)
entry_duration.grid(row=0, column=1)

label_heart_rate = Label(root, text="Heart Rate (bpm):")
label_heart_rate.grid(row=1, column=0, padx=10, pady=10)
entry_heart_rate = Entry(root)
entry_heart_rate.grid(row=1, column=1)

label_age = Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=10)
entry_age = Entry(root)
entry_age.grid(row=2, column=1)

label_weight = Label(root, text="Weight (kg):")
label_weight.grid(row=3, column=0, padx=10, pady=10)
entry_weight = Entry(root)
entry_weight.grid(row=3, column=1)

label_body_temperature = Label(root, text="Body Temperature:")
label_body_temperature.grid(row=4, column=0, padx=10, pady=10)
entry_body_temperature = Entry(root)
entry_body_temperature.grid(row=4, column=1)

button_predict = Button(root, text="Predict Calories", command=predict_calories)
button_predict.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()