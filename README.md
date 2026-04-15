# Exploratory Data Analysis of Diabetes Dataset

## Overview
This project performs Exploratory Data Analysis (EDA) on a diabetes dataset to uncover patterns, trends, and relationships between various health indicators and diabetes outcomes.

## Objectives
- Understand the dataset structure and features  
- Clean and preprocess the data  
- Handle missing and invalid values  
- Perform statistical analysis  
- Visualize data for better insights  
- Build an interactive exploration interface  

## Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Plotly  
- ipywidgets  

## Dataset
The dataset includes medical attributes such as:
- Glucose  
- Blood Pressure  
- BMI  
- Insulin  
- Age  
- Outcome  

## Steps Performed

### Data Loading
- Imported dataset using Pandas  
- Checked structure and data types  

### Data Cleaning
- Replaced invalid zero values with NaN  
- Filled missing values using median  

### Exploratory Data Analysis
- Used `.describe()` for statistical summary  
- Checked missing values  
- Analyzed distributions  

### Data Visualization
- Histograms and distribution plots  
- Correlation analysis  
- Seaborn and Plotly visualizations  

### Interactive Analysis
- Used ipywidgets for dynamic exploration  

## Key Insights
- Glucose is a strong indicator of diabetes  
- BMI and insulin show meaningful patterns  
- Data cleaning improves analysis quality  

## Future Improvements
- Add machine learning model  
- Deploy using Streamlit  
