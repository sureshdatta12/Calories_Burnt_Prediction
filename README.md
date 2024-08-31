# Calories_Burnt_Prediction

This Python application uses a Tkinter GUI to predict calories burnt during exercise based on user inputs (duration, heart rate, age, weight, and body temperature) using an XGBoost regression model trained on a sample dataset.

# Software Requirements:

1) Operating System: Windows, macOS, or Linux.

2) Python: Version 3.7 or higher.

3) Python Libraries:

   tkinter: Standard Python library for GUI applications.
   
   pandas: For data manipulation (pip install pandas).
   
   numpy: For numerical operations (pip install numpy).
   
   scikit-learn: For data splitting and machine learning utilities (pip install scikit-learn).
   
   xgboost: For XGBoost regression model (pip install xgboost).
   
   IDE or Text Editor: Any Python-compatible IDE like PyCharm, VSCode, or Jupyter Notebook.

# Hardware Requirements:

1) Processor: Dual-core processor (Intel i3 or equivalent) or higher.
   
2) RAM: Minimum 4 GB (8 GB or higher recommended for better performance).
   
3) Storage: At least 100 MB free space (for Python libraries and dataset storage).
   
4) Display: Monitor capable of displaying the GUI properly.

# Additional Notes:
 1) Ensure that the dataset files (exercise.csv and calories.csv) are accessible in the specified paths.
    
 2) The code uses basic GUI components that should run smoothly on most modern hardware setups. However, if you are working with a larger dataset, more RAM may be required for efficient processing.

# How To Run:

1) Install Python:

     Make sure Python (version 3.7 or higher) is installed on your system. You can download it from the official Python website.

2) Install Required Libraries:

     Open a terminal (Command Prompt, PowerShell, or Terminal) and install the necessary libraries using pip:
   
           pip install pandas numpy scikit-learn xgboost

3) Prepare the Dataset:

     Place the exercise.csv and calories.csv datasets in a known directory (make sure they are correctly formatted as expected by the code).

4) Modify the Code Paths:

     Update the file paths in the code to point to the correct location of your datasets. Replace:
   
            df = pd.read_csv(r'C:\path\to\exercise.csv')
            df2 = pd.read_csv(r'C:\path\to\calories.csv')
     with the actual paths where your CSV files are located.

5) Run the Code:

    Save the code in a Python file, e.g., calories_prediction.py.
   
    Run the file from your terminal or command prompt:

       python calories_prediction.py


6) Interact with the GUI:
    A GUI window will appear. 
    
   Enter the required inputs such as Duration (minutes), Heart Rate (bpm), Age, Weight (kg), and Body Temperature.
     
   Click the "Predict Calories" button to see the predicted calories burnt.

7) View the Prediction:

      A message box will display the predicted calories burnt based on the inputs provided.
      

# Outputs:

 ![3](https://github.com/user-attachments/assets/6cfe9764-6fbf-4ced-bd06-34688952c1d5)

 ![4](https://github.com/user-attachments/assets/b98dc131-84b7-452d-a0ce-90feb17fce5f)

 ![5](https://github.com/user-attachments/assets/a47ecda6-b02f-4a1d-aa0a-d2841edad592)



























