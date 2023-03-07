import stream lis as at
import pandas as pandas

st.title(‘Streamlit-Search ranges’)

DATA_URL = https://firebasestorage.googleapis.com/v0/b/centeno-6d1f9.appspot.com/o/imagen%2FIMG_2347.JPG?alt=media&token=e4dadb38-147d-4697-b4c2-81f2f81d11ce


@st.cache
def load_data_byrange (startid, endid):
    data = pd.read_csv (DATA_URL)
    filtered_data_byrange = data [ (data['index'] >= startid) & (data ['index'] <=endid) ]

return filtered_data_byrange

startid = st.text_input ('Start index :')
endid = st.text_input ('End index :')
btnRange = st.button ('Search by range')

if (btnRange):
    filterrbyrange = load_data_byrange (int(startid), int (endid))
    count_row = filterrbyrange.shape [0] #Gives numbre of rows
    st.write (f "Total items : {count_row}")

    st.dataframe(filterrbyrange)
