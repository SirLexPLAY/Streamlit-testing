import streamlit as st
import time

# ---- CONFIGURATION ----
st.set_page_config(page_title="Odkrywanie!", page_icon=":sunglasses:", layout="wide")


# ---- HEADER SECTION ----
with st.container():
    st.title("Odkrywanie ciekawy funkcji zawartych w Streamlit!")
    st.write("Zaczynamy!")


# ---- SIDE SECTION ----
with st.sidebar:
    st.write("Hello!")


# ---- MAIN SECTION ----
with st.container():
    st.write("##")
    if st.button("Włącz spinnera na 5 sekund"):
        with st.spinner("Pokręce się 5 sekund :dizzy:"):
            time.sleep(5)

    st.write("##")
    col1, col2, col3 = st.columns(3)
    col1.metric("Zysk", "70 kr", "-35 kr")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    st.write("##")
    col4, col5, col6 = st.columns(3)
    

    with col4:
        check1 = st.checkbox("1")
    
    with col5:
        check2 = st.checkbox("2")

    with col6:
        check3 = st.checkbox("3")

    if check1 and check2 and check3:
        st.write("Hurra!")
        st.balloons()
    
with st.container():
    st.write("##")
    my_bar = st.progress(0)
    status = st.markdown("0%")

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)
        status.markdown(str(percent_complete + 1) + "%")
        