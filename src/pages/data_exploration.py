import streamlit as st


def load() -> None:
    st.dataframe(info_content_df.head())

    st.dataframe(info_userdata_df.head())

    st.dataframe(log_problem_df.head())
