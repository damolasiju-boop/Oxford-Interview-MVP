import streamlit as st

st.set_page_config(page_title="Oxbridge Interview Bot")

st.title("Mini Oxbridge Interview")
st.caption("Civil Disobedience · Philosophy")

questions = [
    "Is breaking the law ever morally justified?",
    "If a law is democratically voted in, can it still be unjust?",
    "If peaceful protest fails, can violence ever become legitimate?",
    "Who decides when injustice is severe enough to justify force?"
]

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

# Display previous conversation
for i in range(len(st.session_state.answers)):
    st.markdown(f"**Tutor:** {questions[i]}")
    st.markdown(f"**Candidate:** {st.session_state.answers[i]}")

# Ask next question
if st.session_state.step < len(questions):
    st.markdown(f"**Tutor:** {questions[st.session_state.step]}")
    answer = st.text_input("Your answer:")

    if answer:
        st.session_state.answers.append(answer)
        st.session_state.step += 1
        st.rerun()
else:
    st.markdown("**Tutor:** Thank you. That concludes this mini interview.")
