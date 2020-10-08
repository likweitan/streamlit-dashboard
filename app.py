import streamlit as st
import pandas as pd

import src.pages.home as home
import src.pages.data_exploration as data_exploration

# Streamlit encourages well-structured code, like starting execution in a main() function.


def main():
    # Download external dependencies.
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.sidebar.text('Loading...')
    # Load 10,000 rows of data into the dataframe.
    with st.spinner('Reading data...'):
        data = load_data(None)
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
                                  ('Home', 'Data Exploration', 'Content Statistics', 'User Statistics', 'Problem Statistics', 'Check Proficiency'))
    if option == "Home":
        home.load()
    elif option == "Data Exploration":
        data_exploration.load(data)
    elif option == "Content Statistics":
        readme_text.empty()


@st.cache
def load_data(nrows):
    data = [pd.read_csv('https://media.githubusercontent.com/media/likweitan/streamlit-dashboard/main/data/Info_Content.csv'),
            pd.read_csv(
                'https://media.githubusercontent.com/media/likweitan/streamlit-dashboard/main/data/Info_UserData.csv'),
            pd.read_csv('https://media.githubusercontent.com/media/likweitan/streamlit-dashboard/main/data/Log_Problem.csv', nrows=10000), ]
    return data


if __name__ == "__main__":
    main()
