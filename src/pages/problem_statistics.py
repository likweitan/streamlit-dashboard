import streamlit as st
import altair as alt

import pandas as pd
import numpy as np


def load(data):
    st.header('🎲 Data Exploration')
    with st.spinner('Loading graph...'):
        plot_play_count_graph(data[0], data[1], data[2])


def plot_play_count_graph(info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    datecount_df = (pd.to_datetime(log_problem_df['timestamp_TW'], format='%Y-%m-%d %H:%M:%S %Z')
                    .dt.floor('d')
                    .value_counts()
                    .rename_axis('date')
                    .reset_index(name='count')
                    .sort_values('date'))

    st.header("**♟** Log Problem **♟**")
    st.write('From the chart below, we could see that the number of users attempt the question is getting lower.')

    chart = alt.Chart(datecount_df).mark_line().encode(
        x='date',
        y='count'
    )
    st.altair_chart(chart, use_container_width=True)
