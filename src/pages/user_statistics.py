import streamlit as st
import altair as alt

import pandas as pd
import numpy as np


def load(data):
    st.header('🎲 Data Exploration')
    users = find_user(data[1], data[2])
    st.sidebar.header('User')
    user = st.sidebar.selectbox('Please select an user', users)
    plot_difficulty(user, data[0], data[1], data[2])
    plot_gender(user, data[0], data[1], data[2])


@st.cache
def find_user(info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    merge_df = log_problem_df.merge(info_userdata_df, how='left', on='uuid')
    users = merge_df.uuid.head(50).values
    return users


def highlight_correct(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == 1
    return ['background-color: green' if v else '' for v in is_max]


def plot_gender(user, info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    merge_df = log_problem_df.merge(info_userdata_df, how='left', on='uuid')
    course = st.sidebar.selectbox(
        'Select Course', merge_df.ucid[merge_df['uuid'] == user].drop_duplicates().values)
    st.header("**♟** Learning Path **♟**")
    st.write('From the chart below, we could see that the number of users attempt the question is getting lower.')
    # Lets randomly pick a user and an exercise and observe the learning process!
    learning_path = log_problem_df[(
        log_problem_df['uuid'] == user) & (
        log_problem_df['ucid'] == course)]

    learning_path = learning_path[['timestamp_TW',
                                   'problem_number', 'is_correct']].copy()
    st.write(learning_path.sort_values(
        'problem_number').style.apply(highlight_correct))

    total_rows = learning_path.shape[0]
    st.write('The user has tried ' + str(total_rows) +
             ' times for this content.')


def plot_difficulty(user, info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    merge_df = log_problem_df.merge(info_userdata_df, how='left', on='uuid')
    merge_df = merge_df.merge(info_content_df, how='left', on='ucid')

    group_difficulty = merge_df[merge_df['uuid'] ==
                                user].drop_duplicates(subset=['uuid', 'ucid'])

    st.bar_chart(group_difficulty['difficulty'].value_counts())

    st.write(group_difficulty)
