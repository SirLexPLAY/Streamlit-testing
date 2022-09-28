import streamlit as st
import numpy as np

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# --- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Dawid :wave:")
    st.title("A informatics student in Oslo")
    st.write("I am passionate about Programming")
    st.write("Tell me something about yourself!")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("Loloololo jeg er 22 år gammel.")
    with right_column:
        st.header("I love you")
