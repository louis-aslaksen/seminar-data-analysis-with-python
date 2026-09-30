import streamlit as st
import random
from bulls_and_cows import check_bulls_cows, check_input

#------------------ Settings ------------------#

#Page layout
st.set_page_config(layout="wide")

#Background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #014d4e;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#Command to start game in terminal, ADMIN USE
run_command = """
streamlit run "Bulls and Cows/app_bulls_and_cows.py"
"""

#Title and description
st.markdown(
    "<h1 style='text-align: center;'>Bulls and Cows</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Guess the secret 4-digit number!</p>",
    unsafe_allow_html=True
)

#Divide screen into two columns
left, right = st.columns([2,2])

#------------------ Initiating Variables ------------------#

if "tries" not in st.session_state:
    st.session_state.tries = 0

if "highscore" not in st.session_state:
    st.session_state.highscore = None

if "rndm" not in st.session_state:
    st.session_state.rndm = []

    for i in range(4):
        st.session_state.rndm.append(str(random.randint(0,9)))

if "history" not in st.session_state:
    st.session_state.history = []

#------------------ Game logic ------------------#

with right:

    #Reset guess histroy if not empty
    game_over = (len(st.session_state.history) > 0 and st.session_state.history[-1]["Bulls"] == 4)
    
    #Guess input
    with st.form("guess_form", clear_on_submit=True):
        guess = st.text_input("Enter your number:", key="guess_input", disabled=game_over)
        submitted = st.form_submit_button("Guess", disabled=game_over)

    if submitted:
        #Check correct input, if true start game logic
        if check_input(guess):
            bulls, cows = check_bulls_cows(st.session_state.rndm,list(guess))
            st.session_state.tries += 1

            #List of all guesses made, without is is quite hard to play :)
            st.session_state.history.append({
                "Guess": guess,
                "Bulls": bulls,
                "Cows": cows
            })

            #End of Game
            if bulls == 4:
                st.write("You won! It took you " + str(st.session_state.tries) + " tries")
                st.balloons()

                #Set highscore if needed
                if st.session_state.highscore is None:
                    st.session_state.highscore = st.session_state.tries
                elif st.session_state.highscore > st.session_state.tries:
                    st.session_state.highscore = st.session_state.tries

            #Game contiunes, write bulls and cows
            else:
                st.write("You have " + str(bulls) + " bulls and " + str(cows) + " cows. Try again!")
            
        #Wrong input, ask for new Input
        else:
            st.write("Your input must consist of 4 digits.")

    #Check if game is over and reset
    if st.session_state.history:
        if st.session_state.history[-1]["Bulls"] == 4:
            if st.button("New Game"):
                st.session_state.tries = 0
                st.session_state.history = []
                st.session_state.rndm = []
                st.session_state.excluded = []
                st.session_state.notes = ""

                for i in range(4):
                    st.session_state.rndm.append(str(random.randint(0,9)))

                st.rerun()
                    

    #Write highscore
    if st.session_state.highscore is not None:
        st.write("🏆 Your highscore is: " + str(st.session_state.highscore) + " tries.")

    st.table(st.session_state.history)

#------------------ Player notes ------------------#

with left:
    #List where player can note digits to exclude
    excluded = st.multiselect(
        "❌ Excluded digits, here you can write down digits you think won't appear in the secret number",
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], key = "excluded"
        )
    excluded = sorted(excluded)
    
    #Space for player to take notes
    st.text_area("📝 Notes", key = "notes")