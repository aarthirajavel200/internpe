import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Title
st.title("Car Price Prediction App")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the file
    df = pd.read_csv(uploaded_file)
    
    # Display raw data
    st.write("Uploaded data:")
    st.dataframe(df)

    # Data cleaning
    if 'kms_driven' in df.columns and 'Price' in df.columns and 'fuel_type' in df.columns:
        # Cleaning 'kms_driven'
        df['kms_driven'] = (
            df['kms_driven']
            .astype(str)
            .str.replace(' kms', '', regex=False)
            .str.replace(',', '', regex=False)
        )
        df['kms_driven'] = pd.to_numeric(df['kms_driven'], errors='coerce')

        # Cleaning 'Price'
        df = df[df['Price'] != 'Ask for price']
        df['Price'] = df['Price'].str.replace(',', '', regex=False)
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        # Drop rows with missing values
        df = df.dropna(subset=['kms_driven', 'Price'])

        # Label Encoding for 'fuel_type'
        label_encoder = LabelEncoder()
        df['fuel_type'] = label_encoder.fit_transform(df['fuel_type'])

        # Display cleaned data
        st.write("Cleaned data:")
        st.dataframe(df)

        # Features and target
        features = ['kms_driven', 'fuel_type']
        target = ['Price']
        st.write(df.dtypes)
        X = df[features]
        Y = df[target]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

        # Sidebar for algorithm selection
        st.sidebar.title("Model Selection")
        algorithm = st.sidebar.selectbox("Choose an algorithm", ("Linear Regression", "Decision Tree", "Random Forest"))

        # Model selection
        if algorithm == "Linear Regression":
            model = LinearRegression()
         
        elif algorithm == "Decision Tree":
            model = DecisionTreeRegressor()
              
        elif algorithm == "Random Forest":
            model = RandomForestRegressor()

        # Train the model
        model.fit(X_train, y_train)

        # Predictions and performance
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        st.write(f"Mean Squared Error ({algorithm}): {mse}")

    else:
        st.error("Dataset must contain 'kms_driven', 'Price', and 'fuel_type' columns.")
