
import random
import streamlit as st

st.set_page_config(page_title="Guess My Number")

LEVELS = {
    "Easy": 50,
    "Normal": 100,
    "Hard": 1000
}


def new_game():
    maximum = LEVELS[st.session_state.difficulty]
    st.session_state.secret = random.randint(1, maximum)
    st.session_state.guesses = []
    st.session_state.low = 1
    st.session_state.high = maximum
    st.session_state.won = False
    st.session_state.message = ""
    st.session_state.guess_input = 1


def check_guess():
    if st.session_state.won:
        return

    guess = st.session_state.guess_input
    secret = st.session_state.secret

    if guess in st.session_state.guesses:
        st.session_state.message = "You already guessed this number."
        return

    st.session_state.guesses.append(guess)

    if guess == secret:
        st.session_state.won = True
        st.session_state.message = (
            f"Correct! The number was {secret}. "
            f"You used {len(st.session_state.guesses)} guesses."
        )

    elif guess < secret:
        st.session_state.low = max(st.session_state.low, guess + 1)
        st.session_state.message = "Too low. Try a higher number."

    else:
        st.session_state.high = min(st.session_state.high, guess - 1)
        st.session_state.message = "Too high. Try a lower number."


if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Normal"

if "secret" not in st.session_state:
    new_game()


st.title("Guess My Number")
st.write("Guess the secret number.")

st.selectbox(
    "Difficulty",
    options=list(LEVELS),
    key="difficulty",
    on_change=new_game
)

maximum = LEVELS[st.session_state.difficulty]

st.write(f"Choose a number between 1 and {maximum}.")
st.write(f"Attempts: {len(st.session_state.guesses)}")

if not st.session_state.won:
    st.write(
        f"Possible range: "
        f"{st.session_state.low} - {st.session_state.high}"
    )

with st.form("guess_form"):
    st.number_input(
        "Your guess",
        min_value=1,
        max_value=maximum,
        step=1,
        key="guess_input",
        disabled=st.session_state.won
    )

    st.form_submit_button(
        "Submit",
        on_click=check_guess,
        disabled=st.session_state.won
    )

if st.session_state.message:
    if st.session_state.won:
        st.success(st.session_state.message)
    else:
        st.info(st.session_state.message)

if st.session_state.guesses:
    st.write("Previous guesses:")
    st.write(", ".join(map(str, st.session_state.guesses)))

st.button("New Game", on_click=new_game)
