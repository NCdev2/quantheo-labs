import streamlit as st

# Set the title of the app
st.title("Welcome to Quantheo Labs")

# Add a description
st.write("This is a Streamlit application for Quantheo Labs.")

# Load and display the HTML content
with open("static/index.html", "r") as file:
    html_content = file.read()
    st.components.v1.html(html_content, height=600)

# Add user interaction
if st.button("Learn More"):
    st.write("This button can be used to trigger additional information or actions.")