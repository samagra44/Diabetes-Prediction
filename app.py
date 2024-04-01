import streamlit as st
import numpy as np
import pickle as pk
## loading the Random Forest Classifier Model
with open("saved_model.pkl",'rb') as model_file:
    Ctree = pk.load(model_file)

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🤷🏻",
    layout="centered"
)
st.title("Diabetes Prediction")
# Define the input fields
input_fields = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 
                'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 
                'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 
                'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 
                'Income']

# Get user input for each field
input_data = {}
for field in input_fields:
    input_data[field] = st.number_input(label=f"Enter {field}", value=0.0)

# Display the input data
st.write("Input Data:", input_data)

# Create a submit button
if st.button("Submit"):
    # Convert input data to array
    input_array = np.array([[input_data[field] for field in input_fields]])

    # Assuming 'Ctree' is already defined elsewhere in your code
    # Make a prediction
    prediction = Ctree.predict(input_array)

    # Define the prediction output
    prediction_output = "No Diabetes" if prediction[0] == 0 else "Diabetes"

    # Display the prediction
    st.write("Model Prediction:", prediction_output)