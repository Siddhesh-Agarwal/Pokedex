import streamlit as st
import pokebase as pb
import requests

st.title("Pokedex")
st.write("Search the pokemon you are looking for and you will get the details.")

name = st.text_input("Search Pokemon here:")

if st.button("Search..."):
    st.header("Information")
    
    poke = pb.pokemon(name)
    st.markdown(f"**Name**: {name.title()}")
    
    try:
        st.markdown(f"**Type**:")
        for slot, type_slot in enumerate(poke.types, start=1):
            st.write(f"{slot}. {type_slot.type.name}")
        
        st.markdown(f"**Height**: {poke.height}")
        st.markdown(f"**Weight**: {poke.weight}")
        st.markdown(f"**Base experience**: {poke.base_experience}")

        st.markdown(f"**Abilities**:")
        for sno, ability in enumerate(poke.abilities, start=1):
            st.write(f"{sno}. {ability.ability.name.replace('-', ' ')}")

    except AttributeError:
        st.warning('Pokemon does not exist in the database.')