import time
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
iris_data = load_iris()


data = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

fig = plt.figure()
sns.histplot(data=data, bins=20)
st.pyplot(fig)