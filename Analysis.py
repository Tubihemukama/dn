import streamlit as st
import pandas as pd

# Set page configuration FIRST
st.set_page_config(
    page_title="My App",
    page_icon="🧠",
    layout="wide"
)

st.title("📊 Data Analyzer")

upload = st.file_uploader("Upload an Excel File", type=["xlsx"])

if upload is not None:
    dataset = pd.read_excel(upload)
    st.subheader("Preview of Dataset")
    st.write(dataset.head())

    variable_list = dataset.columns
    numeric_variable_list = dataset.select_dtypes(include="number").columns
    non_numeric_variable_list = dataset.select_dtypes(include=["object", "string", "category"]).columns

   

    # Categorical Summary
    st.subheader("🔠 Non-Numeric Variable Frequency Table")
    def non_numeric_variables():
        all_tables = []
        for var in non_numeric_variable_list:
            frequency_table = dataset[var].value_counts(dropna=False).reset_index()
            frequency_table.columns = ['Category', 'Frequency']
            frequency_table['Percentage'] = (frequency_table['Frequency'] / frequency_table['Frequency'].sum()) * 100
            frequency_table['Percentage'] = frequency_table['Percentage'].round(2)
            frequency_table['Variable'] = var
            frequency_table = frequency_table[['Variable', 'Category', 'Frequency', 'Percentage']]
            all_tables.append(frequency_table)

        combined_table = pd.concat(all_tables, ignore_index=True)
        st.dataframe(combined_table)

    non_numeric_variables()

else:
    st.warning("⚠️ Please upload an Excel file to proceed.")
st.write("Methodius")
