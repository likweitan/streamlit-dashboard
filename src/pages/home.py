import streamlit as st


def load(data) -> None:
    """ The homepage is loaded using a combination of .write and .markdown.
    Due to some issues with emojis incorrectly loading in markdown st.write was
    used in some cases.
    When this issue is resolved, markdown will be used instead.
    """
    # st.image("https://raw.githubusercontent.com/MaartenGr/boardgame/master/images/logo_small.jpg",
    #         use_column_width = True)
    st.title('Assessing the Readiness of HEI in Malaysia to Accept Generation Alpha')

    st.markdown("> A Dashboard for the HEI in Malaysia")
    
    st.header("🎲 The Application")
    st.write("This application is a Streamlit dashboard hosted on Heroku that can be used to explore "
             "the results from Junyi Academy Online.")
    
    st.write("There are "+ str(data[1].shape[0])+" students in total.")

