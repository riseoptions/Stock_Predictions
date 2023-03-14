import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Stock Prices')

data = pd.read_csv('AAPL.csv')
#data = data1[['Open', 'Close', 'Volume']]

with st.sidebar:
    var3 = st.selectbox('Choose stock:', options=['AAPL', 'GOOG', 'MSFT'])
    st.write('Choose the variables for the Scatter Plot')
    var1 = st.selectbox('Choose 1st var', options=list(data.columns))
    var2 = st.selectbox('Choose 2nd var', options=list(data.columns))
    N = st.number_input('Insert a number')
#     st.write('The current number is ', N)
#     D = st.number_input('Insert a number')
#     st.write('The current number is ', D)

st.table(data['Close'].head(10))

df = data['Close']
#df = data[var1]

# st.write(df.columns)

tabs = ['Graph 1', 'Graph 2']
tab1, tab2 = st.tabs(tabs)

with tab1:
    fig, ax = plt.subplots()
    ax.plot(np.array(df), marker = "o")

    plt.title('Title of the plot\nwith two lines')
    st.pyplot(fig)

with tab2:
    fig1, ax = plt.subplots()
    ax.plot(np.array(df))

    plt.title('Title of the plot\nwith two lines')
    st.pyplot(fig1)
