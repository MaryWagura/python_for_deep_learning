import time
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#create a bar chart in matplot and display in streamlit

animals = ['cat', 'dog', 'horse', 'girrafe', 'cow']
heights = [30, 40, 60, 80, 50]
weights = [10, 30, 50, 80, 100]

fig, ax = plt.subplots()

x= np.arange(len(heights))
width = 0.40

ax.bar(x-0.2, heights, width, color='red')
ax.bar(x+0.2, weights, width, color='blue')

ax.legend(['height', 'weight'])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)


