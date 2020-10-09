# Importing the libraries
import streamlit as st

import numpy as np
import pandas as pd


@st.cache
def clean(data):
    data = impute_missing_values(data[0], data[1], data[2])
    return data


def impute_missing_values(info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):

    # replace all NA's with unspecified
    info_userdata_df = info_userdata_df.fillna('unspecified')

    # replace all NA's with false
    log_problem_df = log_problem_df.fillna(False)

    data = [info_content_df, info_userdata_df, log_problem_df]

    return data
