import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Diabetes Dashboard", layout="wide")

# Title
st.title("🧠 Diabetes Data Analysis Dashboard")

# Load data
df = pd.read_csv("diabetes.csv")

# Sidebar filters
st.sidebar.header("Filter Data")

age_range = st.sidebar.slider(
    "Select Age Range",
    int(df.Age.min()),
    int(df.Age.max()),
    (20, 50)
)

df = df[(df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])]

# Show dataset
st.subheader("📄 Dataset Preview")
st.dataframe(df)

# ---------------------------
# 1. Outcome Distribution
# ---------------------------
st.subheader("📊 Diabetes Outcome Distribution")

fig, ax = plt.subplots()
sns.countplot(x="Outcome", data=df, ax=ax)
st.pyplot(fig)

# ---------------------------
# 2. Glucose vs BMI
# ---------------------------
st.subheader("📊 Glucose vs BMI")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Glucose", y="BMI", hue="Outcome", ax=ax)
st.pyplot(fig)

# ---------------------------
# 3. Correlation Heatmap
# ---------------------------
st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# ---------------------------
# 4. BMI Distribution
# ---------------------------
st.subheader("📊 BMI Distribution")

fig, ax = plt.subplots()
sns.histplot(df["BMI"], kde=True, ax=ax)
st.pyplot(fig)

# ---------------------------
# Footer
# ---------------------------
st.write("✔ Built using Streamlit + Python")