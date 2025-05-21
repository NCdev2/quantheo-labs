import streamlit as st
import streamlit.components.v1 as components # Import components
import os

# Set the title of the app
st.title("Quantheo Labs - Celestial Simulation")

# Get the absolute path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the HTML file relative to this script's directory
html_file_path = os.path.join(script_dir, "static", "celestial_simulation.html")

# Read and display the HTML content
try:
    with open(html_file_path, "r") as file:
        html_content = file.read()
    # Display the HTML content in the Streamlit app
    components.html(html_content, height=800) # Use components.html
except FileNotFoundError:
    st.error(f"Error: HTML file not found at {html_file_path}")
    st.error(f"Current script directory: {script_dir}")
    st.error(f"Files in static directory: {os.listdir(os.path.join(script_dir, 'static')) if os.path.exists(os.path.join(script_dir, 'static')) else 'Static directory not found'}")