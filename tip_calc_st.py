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
    bill = st.text_input(
        "What is the total bill? (Enter amount in dollars but without the dollar sign. E.g. enter 150.25 for $150.25)",
        on_change = set_state, args=[3]
        )

    if bill is None:
        set_state(2)

if st.session_state.stage >=3:
    
    tip = st.slider(
        "Please use slider to select the percentage of tip you would like to give.",
        on_change = set_state, args = [4]
        )
    
    st.markdown(f"You have chosen to give a tip of {tip}%")
    
    if tip is None:
        set_state(3)


if st.session_state.stage >=4:
    num_people = st.text_input(
        "How many people are to split the bill?",
        on_change = set_state, args = [5])

    if num_people is None:
        set_state(4)

if st.session_state.stage >=5:
    bill_per_person = (float(bill)*(1+float(tip)/100))/int(num_people)
    st.markdown(f"##### Each person should pay:  :orange[$ {bill_per_person:.2f}]")
    st.button("Start Over", on_click=set_state, args=[0])
