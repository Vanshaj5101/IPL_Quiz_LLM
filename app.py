import streamlit as st
import llm_logic

st.set_page_config(page_title="IPL Trivia Quiz", page_icon=":cricket_game:")

# Title
st.title('IPL Trivia Quiz')

# Sidebar for category and team selection
st.sidebar.title("Quiz Configuaration")
category_selector = st.sidebar.selectbox('Select a Category', ('Bowler', 'Batsman', 'Team', 'All Rounder', 'Wicket Keeper', 'None'))
team_selector = st.sidebar.radio('Select a Team', ('Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
                                                       'Sunrisers Hyderabad', 'Delhi Capitals', 'Gujarat Titans', 'Lucknow Super Giants',
                                                       'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'None'))

if category_selector != "None" and team_selector != "None":
    quiz = llm_logic.generate_quiz(category=category_selector, team=team_selector)
    options = llm_logic.generate_options()
    
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
