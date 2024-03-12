""" 
The Band Name Generator Application powered by Streamlit
"""

import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin")
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    st.write("## Welcome to the Tip Calculator.")
    name = st.text_input('What is your name?', on_change=set_state, args=[2])


if st.session_state.stage >=2:
    st.write(f'Hello {name.capitalize()}!')
    bill = float(st.text_input(
        "What is the total bill? (Enter amount in dollars but without the $ sign. e.g. write 150.20 for $150.20)",
        on_change = set_state, args=[3]
        ))
    st.write(f"You have entered a bill of $ {bill:.2f}")

    if bill is None:
        set_state(2)

if st.session_state.stage >=3:
    tip = float(st.text_input(
        "How much tip would you like to give? (Enter a percentage amount without the '%' sign. E.g. write 10 for 10%)",
        on_change = set_state, args = [4]))
    st.write(f"You have entered a tip of {tip:.2f}%")
    if tip is None:
        set_state(3)


if st.session_state.stage >=4:
    num_people = int(st.text_input(
        "How many people are to split the bill?",
        on_change = set_state, args = [5]))
    if tip is None:
        set_state(4)

if st.session_state.stage >=5:
    bill_per_person = (bill*(1+tip/100))/num_people
    st.markdown(f"Each person should pay: $ {bill_per_person:.2f}")
    st.button("Start Over", on_click=set_state, args=[0])