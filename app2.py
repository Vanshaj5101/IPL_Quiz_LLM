import streamlit as st
import llm_logic

# Cache the function calls to generate_quiz and generate_options
@st.cache_data()
def load_quiz(category, team):
    return llm_logic.generate_quiz(category=category, team=team)

@st.cache_data()
def load_options(category, team):
    return llm_logic.generate_options()

st.set_page_config(page_title="IPL Trivia Quiz", page_icon=":cricket_game:")

# Title
st.title('IPL Trivia Quiz')

# Sidebar for category and team selection
st.sidebar.title("Quiz Configuration")
category_selector = st.sidebar.selectbox('Select a Category', ('Bowler', 'Batsman', 'Team', 'All Rounder', 'Wicket Keeper', 'None'))
team_selector = st.sidebar.radio('Select a Team', ('Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
                                                       'Sunrisers Hyderabad', 'Delhi Capitals', 'Gujarat Titans', 'Lucknow Super Giants',
                                                       'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'None'))

if category_selector != "None" and team_selector != "None":
    # Load quiz and options
    quiz = load_quiz(category_selector, team_selector)
    options = load_options(category_selector, team_selector)
    
    st.markdown("## Quiz Question:")
    st.write(quiz['quiz'])
    
    # Display options
    st.markdown("## Options:")
    st.write(options['options'])

    answer = st.text_input('Enter your answer: ')

    st.markdown("## Result")
    ans_placeholder = st.empty()

    if st.button('Submit Response'):
        response = llm_logic.check_ans(answer)
        ans_placeholder.write(response['response'])

# Add footer or additional information
st.markdown("---")
st.markdown("Built by a cricket lover 🏏")
