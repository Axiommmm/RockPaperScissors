import streamlit as st
import random as rd

if "player_point" not in st.session_state:
    st.session_state.player_point = 0
    st.session_state.opponent_point = 0


@st.dialog("Score")
def result(didWin:str):
    if (didWin == "1"):
        st.write("You won!")
    elif (didWin == "0"):
        st.write("Opponent won!")
    elif(didWin == "equal"):
        st.write("Tie!")
    if st.button("OK"):
        st.rerun()

def rps(player: int, opponent: int) -> str:
    if(player==1 and opponent==3):
        st.session_state.player_point +=1
        return "1"
    elif(player==3 and opponent==1):
        st.session_state.opponent_point +=1
        return "0"
    elif(player > opponent):
        st.session_state.player_point +=1
        return "1"
    elif(player < opponent):
        st.session_state.opponent_point +=1
        return "0"
    elif(player == opponent):
        return "equal"

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="My Point", value=st.session_state.player_point)
with col3:
    st.metric(label="Opponent's Point", value=st.session_state.opponent_point)

opp_choice = rd.randint(1,3)
with col1:
    for _ in range(2): st.write("")
    if st.button("Rock", key=1):
        result(rps(1,opp_choice))
with col2:
    for _ in range(8): st.write("")
    if st.button("Paper", key=2):
        result(rps(2,opp_choice))
with col3:
    for _ in range(2): st.write("")  
    if st.button("Scissors", key=3):
        result(rps(3,opp_choice))
