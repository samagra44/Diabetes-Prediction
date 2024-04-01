# Diabetes Prediction Web Application

This web application is designed to predict the likelihood of diabetes based on various health-related factors. Users can input their health information, and the application will provide a prediction indicating whether the individual is likely to have diabetes or not.

## Repository Structure

```
├── data/
│   └── diabetes_binary_health_indicators_BRFSS2015.csv      # Dataset file
├── notebooks/
│   └── Diabetes_Prediction.ipynb  # Jupyter notebook with data exploration and model building
├── models/
│   └── saved_model.pkl                 # Pickled Decision Tree Classifier model
│                     
├── README.md                            # Project README file
└── requirements.txt                     # Python dependencies
```

## Input Features

The following health-related factors are considered as input features for the prediction:

1. **HighBP**: High blood pressure
2. **HighChol**: High cholesterol 
3. **CholCheck**: Cholesterol check
4. **BMI**: Body Mass Index
5. **Smoker**: Smoking status 
6. **Stroke**: History of stroke
7. **HeartDiseaseorAttack**: History of heart disease or heart attack 
8. **PhysActivity**: Physical activity level 
9. **Fruits**: Consumption of fruits 
10. **Veggies**: Consumption of vegetables (
11. **HvyAlcoholConsump**: Heavy alcohol consumption 
12. **AnyHealthcare**: Access to any healthcare services 
13. **NoDocbcCost**: No doctor because of cost 
14. **GenHlth**: General health rating 
15. **MentHlth**: Mental health rating 
16. **PhysHlth**: Physical health rating 
17. **DiffWalk**: Difficulty in walking 
18. **Sex**: Gender 
19. **Age**: Age of the individual
20. **Education**: Level of education 
21. **Income**: Household income level 

## Prediction

The model predicts whether an individual is likely to have diabetes based on the input features.

## How to Use

1. **Input Data**: Enter the values for each of the input features in the provided fields.
2. **Submit**: Click the "Submit" button to generate the prediction.
3. **Prediction**: The prediction will be displayed indicating whether the individual is likely to have diabetes or not.

## About the Model

The prediction model is trained using a decision tree classifier. It analyzes the input features to determine the likelihood of diabetes based on historical data.

## Technologies Used

- Python
- Streamlit
- NumPy
- Scikit-learn
## Output

<p align="center">
<img src="https://github.com/samagra44/Diabetes-Prediction/assets/77968722/fc8d320f-ae66-4b58-b293-a4f3e0df2c81" width=700 height=300 alt="animated"/>
</p>

## Installation

To run this web application locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `streamlit run app.py`.

---
