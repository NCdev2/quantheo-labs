import streamlit as st
import streamlit.components.v1 as components
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the project root directory (one level up from script_dir)
project_root = os.path.dirname(script_dir)

# --- Page Setup ---
st.set_page_config(layout="wide") # Use wide mode for more space

# --- Sidebar for Page Selection ---
st.sidebar.title("Navigation")
selected_page = st.sidebar.selectbox(
    "Choose a visualization:",
    ["Celestial Simulation", "Maths Visualization", "Chemistry Visualization", "Biology Visualization"]
)

# --- Determine HTML file path and title based on selection ---
if selected_page == "Celestial Simulation":
    st.title("Quantheo Labs - Celestial Simulation")
    # Path relative to the script's directory
    html_file_path_to_try = os.path.join(script_dir, "static", "celestial_simulation.html")
elif selected_page == "Maths Visualization":
    st.title("Quantheo Labs - Maths Visualization")
    # Path relative to project root (one level up from script_dir)
    html_file_path_to_try = os.path.join(project_root, "maths.html")
elif selected_page == "Chemistry Visualization":
    st.title("Quantheo Labs - Chemistry Visualization")
    # Path relative to project root (one level up from script_dir)
    html_file_path_to_try = os.path.join(project_root, "chemistry.html")
elif selected_page == "Biology Visualization":
    st.title("Quantheo Labs - Biology Visualization")
    # Path relative to project root (one level up from script_dir)
    html_file_path_to_try = os.path.join(project_root, "biology.html")
else:
    st.error("Invalid page selected.")
    st.stop()


# --- Load and Display HTML ---
try:
    with open(html_file_path_to_try, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    components.html(html_content, height=800, scrolling=True) 

except FileNotFoundError as e:
    st.error(f"Error: HTML file not found for {selected_page}.")
    st.error(f"Attempted path: {html_file_path_to_try}")
    st.error(f"Underlying error: {e}")
    st.error(f"Current Working Directory (os.getcwd()): {os.getcwd()}")
    st.error(f"Script directory (os.path.dirname(os.path.abspath(__file__))): {script_dir}")
    st.error(f"Project root (calculated): {project_root}")

    # List files in script_dir and project_root for debugging
    try:
        st.error(f"Files in script directory ({script_dir}): {os.listdir(script_dir)}")
        st.error(f"Files in project root ({project_root}): {os.listdir(project_root)}")
        static_dir_path = os.path.join(script_dir, "static")
        if os.path.exists(static_dir_path):
            st.error(f"Files in static directory ({static_dir_path}): {os.listdir(static_dir_path)}")
        else:
            st.error(f"Static directory not found at: {static_dir_path}")
    except Exception as list_e:
        st.error(f"Could not list directory contents: {list_e}")

except Exception as e_general:
    st.error(f"!!! An unexpected error occurred for {selected_page} !!!")
    st.error(f"Path attempted: {html_file_path_to_try}")
    st.error(f"Error type: {type(e_general).__name__}")
    st.error(f"Error details: {e_general}")
    st.error(f"Current Working Directory (os.getcwd()): {os.getcwd()}")
    st.error(f"Script directory: {script_dir}")
    st.error(f"Project root: {project_root}")