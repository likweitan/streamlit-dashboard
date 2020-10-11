import streamlit as st
import altair as alt

import pandas as pd
import numpy as np


def load(data):
    st.title('🎲 User Statistics')
    merge_df = merge_all(data[0], data[1], data[2])
    users = find_user(merge_df)
    st.sidebar.header('User')
    user = st.sidebar.selectbox('Please select an user', ['Student A','Student B','Student C','Student D','Student E'])
    switcher = {
        'Student A': "Kpq2q+eKw/O+6/jLs3XJosgmI7weEJxJZdnkKTbbF8I=",
        'Student B': "0+VU/Zb0Q96uoByuRhl7r9bJuJO6CKWpsmNMEuijSzc=",
        'Student C': "g8DnYvIqpolw10XlwWeIWv6NbDPByUbmgH8EshJqBns=",
        'Student D': "kSyUTFlepsYUD723IPL/jEZ520xaKbscrBmNtBUFR1o=",
        'Student E': "XMFbFA7C49+LRhUddhelfPpA6F5dbOoxeyL3eYbuTlY="
    }
    user_id = switcher.get(user,"Invalid")

    st.write(user_id)
    subjects = find_subject(user_id, merge_df)
    st.sidebar.header('Subjects')
    subject_id = st.sidebar.selectbox('Please select a subject', subjects)

    topics = find_topic(user_id, subject_id, merge_df)
    st.sidebar.header('Topics')
    topic_id = st.sidebar.selectbox('Please select a topic', topics)

    contents = find_content(user_id, subject_id, topic_id, merge_df)
    st.sidebar.header('Exercise')
    content = st.sidebar.selectbox('Please select a exercise', contents)
    # with st.spinner('Plotting...'):
    #    plot_difficulty(user, data[0], data[1], data[2])
    plot_gender(user_id, content, data[0], data[1], data[2])

    #st.write(average_score(user, merge_df))


@st.cache(show_spinner=False)
def merge_all(info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    merge_df = log_problem_df.merge(info_userdata_df, how='left', on='uuid')
    merge_df = merge_df.merge(info_content_df, how='left', on='ucid')
    return merge_df


@st.cache(show_spinner=False)
def find_user(merge_df: pd.DataFrame):
    users = merge_df.uuid.head(5).values
    return users

@st.cache(show_spinner=False)
def find_subject(user, merge_df: pd.DataFrame):
    subjects = merge_df.level3_id[merge_df['uuid'] == user].drop_duplicates().values
    return subjects

@st.cache(show_spinner=False)
def find_topic(user, subject, merge_df: pd.DataFrame):
    topics = merge_df.level4_id[(merge_df['uuid'] == user) & (merge_df['level3_id'] == subject)].drop_duplicates().values
    return topics

@st.cache(show_spinner=False)
def find_content(user, subject, topic, merge_df: pd.DataFrame):
    contents = merge_df.ucid[(merge_df['uuid'] == user) & (merge_df['level3_id'] == subject) & (merge_df['level4_id'] == topic)].drop_duplicates().values
    return contents


def highlight_correct(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == 1
    return ['background-color: green' if v else '' for v in is_max]


def highlight_level(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == 4
    return ['background-color: yellow' if v else '' for v in is_max]


def plot_gender(user, content, info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
    st.header("**♟** Learning Path **♟**")
    st.write('From the chart below, we could see that the number of users attempt the question is getting lower.')
    # Lets randomly pick a user and an exercise and observe the learning process!
    learning_path = log_problem_df[(
        log_problem_df['uuid'] == user) & (
        log_problem_df['ucid'] == content)]

    learning_path = learning_path[[
        'timestamp_TW', 'problem_number', 'total_sec_taken', 'total_attempt_cnt', 'used_hint_cnt', 'is_correct', 'level']].reset_index().copy()

    scatter_plot = alt.Chart(learning_path).mark_circle(size=60).encode(
        x='problem_number',
        y='total_sec_taken',
        color='is_correct',
        tooltip=['problem_number', 'total_sec_taken',
                 'used_hint_cnt', 'is_correct']
    )

    st.altair_chart(scatter_plot, use_container_width=True)

    st.write(learning_path.sort_values(
        'problem_number').style.apply(highlight_correct, subset=['is_correct']).apply(highlight_level, subset=['level']))

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


def average_score(user, merge_df: pd.DataFrame):
    x = pd.pivot_table(merge_df[merge_df['uuid'] == user], index=['ucid'],
                       columns=['is_correct'], aggfunc=np.mean)
    return x

# def plot_total_sec_taken(user, info_content_df: pd.DataFrame, info_userdata_df: pd.DataFrame, log_problem_df: pd.DataFrame):
