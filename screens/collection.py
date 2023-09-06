import streamlit as st
import pandas as pd

def Collection_Screen():
    df = pd.read_csv("data/raw/VN_housing_dataset.csv")

    st.title("Hanoi Real Estate App")
    
    st.image("https://images.pexels.com/photos/1546168/pexels-photo-1546168.jpeg?cs=srgb&dl=pexels-david-mcbee-1546168.jpg&fm=jpg")

    st.markdown("""
    This app allows users to see the analysis of Hanoi's real estate, 
    predict property prices, and search for properties.
    """)

    st.subheader("Dataset is collected from Kaggle")
    st.markdown("👉 [Visit the dataset on Kaggle](https://www.kaggle.com/datasets/ladcva/vietnam-housing-dataset-hanoi?select=VN_housing_dataset.csv&fbclid=IwAR1rf0QHrY45ycc8gA_GeFE9NuRlh41_RIkrNbSB5-0t_vYw79L6PVljvGs)")

    # Display the DataFrame
    st.subheader("Dataset Preview:")
    st.write("Number of Rows:", df.shape[0])
    st.write("Number of Columns:", df.shape[1])
    st.dataframe(df)

