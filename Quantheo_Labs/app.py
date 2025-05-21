import streamlit as st
import os

# Set the title of the app
st.title("Quantheo Labs - Celestial Simulation")

# Load the HTML content from the static file
html_file_path = os.path.join("static", "celestial_simulation.html")

# Read and display the HTML content
with open(html_file_path, "r") as file:
    html_content = file.read()

# Display the HTML content in the Streamlit app
st.components.v1.html(html_content, height=800)