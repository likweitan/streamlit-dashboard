import streamlit as st


def load(data):
    st.header('🎲 Predict Level of Student in the Course')
    st.slider('Number of Problems attempted',0,600,key='problem_number')

    st.sidebar.slider('Average Total Second Taken',0,50,key='total_sec_taken')

    st.sidebar.slider('Average Attempt of the questions',0,50,key='total_attempt_cnt')

    st.sidebar.slider('Number of Problems attempted',0,50,key='used_hint_cnt')

    st.slider('Number of Problems attempted',0,11,key='is_upgrade')
    
    st.sidebar.slider('Number of Problems attempted',0,50,key='points')

    st.sidebar.slider('Number of Problems attempted',0,50,key='badges_cnt')
    
    st.write('### The predicted level of the student is')
    st.write('# Level 4')