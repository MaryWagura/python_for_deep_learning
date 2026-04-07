import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

col_names = ['column1', 'column2', 'column3']

data = pd.DataFrame(np.random.randint(30, size=(30,3)), columns = col_names)

'line graph'
st.line_chart(data)

'Bar graph:'
st.bar_chart(data)