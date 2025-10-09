import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Financial News Explorer 📰")

# Load processed data
df = pd.read_csv("../data/cnbc_headlines_clustered_processed.csv")

# Show data
st.subheader("Data Preview")
st.dataframe(df.head())

# Cluster distribution
st.subheader("Cluster Distribution")
fig, ax = plt.subplots()
df['cluster'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Filter headlines by cluster
st.subheader("Browse Headlines by Cluster")
cluster_id = st.selectbox("Select Cluster", df['cluster'].unique())
filtered = df[df['cluster'] == cluster_id][['Headlines']].head(20)
st.write(filtered)
