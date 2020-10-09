import streamlit as st
import pandas as pd

import src.models.data_preprocessing as data_preprocessing

import src.pages.home as home
import src.pages.data_exploration as data_exploration
import src.pages.problem_statistics as problem_statistics
import src.pages.content_statistics as content_statistics
import src.pages.user_statistics as user_statistics
import src.pages.user_activities as user_activities
# Streamlit encourages well-structured code, like starting execution in a main() function.


def main():
    st.beta_set_page_config(
        page_title='Assessing the Readiness', page_icon='https://i.ibb.co/vxwPL94/image.png></a>', layout='centered')
    # Download external dependencies.
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data()
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("")

    # Render the readme as markdown using st.markdown.
    # readme_text = st.markdown("Make sure it has the structure as seen below with the exact same column names"
    #                         ", same structure for scoring points, same structure for players that participated, and "
    #                          "make sure to use the same date format. Any changes to this structure will break the "
    #                         "application. ")

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("Menu")
    option = st.sidebar.selectbox('Please select a page',
                                  ('Home', 'Problem Statistics', 'Content Statistics', 'User Statistics', 'User Activities', 'Check Proficiency'))

    if option == "Home":
        home.load()
    elif option == "Problem Statistics":
        # with st.spinner('Cleaning data...'):
        #    data = data_preprocessing.clean(data)
        problem_statistics.load(data)
    elif option == "Content Statistics":
        content_statistics.load(data)
    elif option == "User Statistics":
        user_statistics.load(data)
    elif option == "User Activities":
        user_activities.load(data)
    elif option == "Check Proficiency":
        st.write('Not yet')
        st.balloons()


@st.cache(persist=True, show_spinner=False)
def load_data():
    data = [pd.read_csv('https://media.githubusercontent.com/media/likweitan/streamlit-dashboard/main/data/Info_Content.csv'),
            pd.read_csv(
                'https://media.githubusercontent.com/media/likweitan/streamlit-dashboard/main/data/Info_UserData.csv'),
            pd.read_csv('https://media.githubusercontent.com/media/likweitan/streamlit-dashboard/main/data/Log_Problem.csv'), ]
    return data


if __name__ == "__main__":
    main()
