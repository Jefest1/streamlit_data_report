# get libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
# import sweetviz as sv
from pandas_profiling import ProfileReport

# set page configurations
st.set_page_config(page_title='Data Profiling', layout='wide')

# Get the fonts of the site
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sour+Gummy:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    
    <style>
            // <uniquifier>: Use a unique and descriptive class name
            // <weight>: Use a value from 100 to 900

            .sour-gummy-<uniquifier> {
            font-family: "Sour Gummy", serif;
            font-optical-sizing: auto;
            font-weight: <weight>;
            font-style: normal;
            font-variation-settings:
                "wdth" 100;
            }
    </style>
""", unsafe_allow_html=True)


# get the sidebar read
with st.sidebar:
    file = st.file_uploader("Please upload file", ['csv', 'xlxs'])
    st.write("Modes of operation")
    min_ = st.checkbox("Do you want minimal Report")
# get the profile report of the data
try:
    file = pd.read_csv(file)

    with st.spinner("Analysing Data"):
        report = ProfileReport(file, minimal=min_, explorative=True)
        st_profile_report(report)
except:
    f"No File Opened"
