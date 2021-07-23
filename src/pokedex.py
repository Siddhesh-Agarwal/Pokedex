import streamlit as st
import pokebase as pb
import requests, json

st.title("Pokedex")
st.write("Search the pokemon you are looking for and you will get the details.")

name = st.text_input("Search Pokemon here:")

if st.button("Search..."):
    pass