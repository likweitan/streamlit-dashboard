import streamlit as st


def load() -> None:
    """ The homepage is loaded using a combination of .write and .markdown.
    Due to some issues with emojis incorrectly loading in markdown st.write was
    used in some cases.
    When this issue is resolved, markdown will be used instead.
    """
    # st.image("https://raw.githubusercontent.com/MaartenGr/boardgame/master/images/logo_small.jpg",
    #         use_column_width = True)
    st.markdown("> A Dashboard for the HEI in Malaysia")
    st.write("The impact of technology in education is getting more common. In the UK, most of the children start to learn coding skills from the age of 5. Generation Alpha will be very different from traditional college students. Technologies will be largely driven in education and educators need to learn how to adapt to it. The traditional method of teaching and learning might not be effective and efficient for Generation Alpha. Institutional culture needs to be changed to prepare the arrival of Generation Alpha students. In a technology-driven period, students need to learn problem-solving skills to help themselves how to think not what to think, and collaboration skills to collaborate with peers around the world. What will the Generation Alpha students behave in higher education? How to define that an institution is ready to accept Generation Alpha? These questions can be answered by finding the unique pattern of generation z using predictive analytics. The proposed system is a dashboard that allows Higher Education Institution (HEI) to capture and analyse useful insights and improve decision making from the student data.")
    st.markdown("<div align='center'><br>"
                "<img src='https://img.shields.io/badge/MADE%20WITH-PYTHON%20-red?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/SERVED%20WITH-Heroku-blue?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/DASHBOARDING%20WITH-Streamlit-green?style=for-the-badge'"
                "alt='API stability' height='25'/></div>", unsafe_allow_html=True)
    for i in range(3):
        st.write(" ")
    st.header("🎲 The Application")
    st.write("This application is a Streamlit dashboard hosted on Heroku that can be used to explore "
             "the results from board game matches that I tracked over the last year.")
    st.write("There are currently four pages available in the application:")
    st.subheader("♟ General Statistics ♟")
    st.markdown("* This gives a general overview of the data including frequency of games over time, "
                "most games played in a day, and longest break between games.")
    st.subheader("♟ Player Statistics ♟")
    st.markdown("* As you play with other people it would be interesting to see how they performed. "
                "This page allows you to see, per player, an overview of their performance across games.")
    st.markdown("* This also includes a one-sample Wilcoxon signed-rank test to test if a player performs "
                "significantly better/worse than the average for one board game.")
    st.subheader("♟ Head to Head ♟")
    st.markdown("* I typically play two-player games with my wife and thought it would be nice to include a "
                "head to head page. This page describes who is the better of two players between and within games.")
    st.subheader("♟ Explore Games ♟")
    st.markdown("* This page serves to show statistics per game, like its distribution of scores, frequency of "
                "matches and best/worst players.")
