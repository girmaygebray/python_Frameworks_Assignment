import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the correct path for the dataset
BASE_DIR = r"C:\Users\ai'r\Desktop\PLP Academy\python\Week8\Frameworks_Assignment"
DATA_PATH = os.path.join(BASE_DIR, "data", "metadata.csv")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# App Title and Description
st.title("📊 CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (`metadata.csv`)")

# Sidebar filter
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Select year range", 2015, 2025, (2019, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications by Year
st.subheader("Publications Over Time")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Sample Data
st.subheader("Sample Data")
st.dataframe(filtered[['title', 'authors', 'journal', 'year']].head(10))
