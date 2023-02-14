import streamlit as at
import pandas as pandas
st.title ("search names")
DATA_URL = "dataset.csv"

@st.cache
def load_data_byname (name):
    data = pd.read_csv(DATA_URL) #read csv
    filtered_data_byname = data [data["name"].str.contains(name)]
    return filtered_data_byname #return the dataframe

myname = st.text_input ("nombre: ")
if (myname):
    filteredbyname = load_data_byname (myname)
    count_now = filteredbyname.shape [0]
    st.write (f"total names : {count_now}")
    st.dataframe (filteredbyname)