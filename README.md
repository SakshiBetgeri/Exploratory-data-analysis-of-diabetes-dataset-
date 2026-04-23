# Exploratory Data Analysis of Diabetes Dataset

## Overview
This project performs Exploratory Data Analysis (EDA) on a diabetes dataset to uncover patterns, trends, and relationships between various health indicators and diabetes outcomes.  
An interactive Streamlit dashboard is also developed to enable real-time data exploration.

## Objectives
- Understand the dataset structure and features  
- Clean and preprocess the data  
- Handle missing and invalid values  
- Perform statistical analysis  
- Visualize data for better insights  
- Build an interactive dashboard  

## Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Plotly  
- Streamlit  

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
- Explored relationships between variables  

### Data Visualization
- Histograms and distribution plots  
- Scatter plots for feature relationships  
- Correlation heatmap  
- Seaborn and Plotly visualizations  

### Interactive Dashboard (Streamlit)
- Built using Streamlit for real-time interaction  
- Age-based filtering using slider  
- Outcome distribution visualization  
- Glucose vs BMI analysis  
- Correlation heatmap  
- BMI distribution  

## Key Insights
- Glucose is a strong indicator of diabetes  
- BMI and insulin show meaningful patterns  
- Data cleaning improves analysis quality  

## Future Improvements
- Add machine learning models for prediction  
- Enhance dashboard with more filters and KPIs  
- Deploy the dashboard online

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
