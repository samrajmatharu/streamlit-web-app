import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a simple app hosted directly from GitHub.')

if st.button('Click me'):
    st.write('Thanks for clicking!')
