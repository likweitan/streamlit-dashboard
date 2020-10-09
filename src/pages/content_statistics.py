import streamlit as st
import altair as alt

import pandas as pd
import numpy as np


def load(data):
    st.title('🎲 Content Statistics')
    with st.spinner('Loading graph...'):
        plot_play_count_graph(data[0], data[1], data[2])
    plot_sum(data[0], data[1], data[2])


def plot_play_count_graph(info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    st.header("**♟** Content Statistics **♟**")
    st.write("This page contains basic exploratory data analyses for the purpose of getting a general feeling of what the data contains.")

    chart = alt.Chart(info_content_df).mark_bar().encode(
        x='count()',
        y='learning_stage',
        color='difficulty',
        order=alt.Order(
            # Sort the segments of the bars by this field
            'learning_stage',
            sort='ascending'
        )

    ).properties(
        width=1500,
        height=200
    )

    st.altair_chart(chart, use_container_width=True)


def plot_connect():
    st.write('aa')


def plot_sum(info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    x = pd.pivot_table(log_problem_df, index=['ucid', 'uuid'],
                       values=['total_sec_taken'], aggfunc=max).sort_values('total_sec_taken').reset_index()
    y = pd.pivot_table(x, index=['ucid'], values=[
                       'total_sec_taken'], aggfunc=np.mean).sort_values('total_sec_taken')

    st.bar_chart(y)
