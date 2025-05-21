import streamlit as st
import streamlit.components.v1 as components
import os

st.title("Quantheo Labs - Celestial Simulation")

# Path construction
# Option 1: Relative to assumed CWD (repository root)
# On Streamlit Cloud, CWD is often /mount/src/your-repo-name
# Target: your-repo-name/Quantheo_Labs/static/celestial_simulation.html
path_relative_to_repo_root = os.path.join("Quantheo_Labs", "static", "celestial_simulation.html")

# Option 2: Relative to the script's directory using __file__
# __file__ should be /mount/src/your-repo-name/Quantheo_Labs/app.py
# script_dir_file_based should be /mount/src/your-repo-name/Quantheo_Labs
script_dir_file_based = os.path.dirname(os.path.abspath(__file__))
path_file_based = os.path.join(script_dir_file_based, "static", "celestial_simulation.html")

# We'll try the __file__ based path first as it's generally more robust if __file__ is reliable.
html_file_path_to_try = path_file_based

try:
    st.info(f"[DEBUG] Attempting to open: {html_file_path_to_try}")
    st.info(f"[DEBUG] Path exists: {os.path.exists(html_file_path_to_try)}")

    with open(html_file_path_to_try, "r", encoding="utf-8") as file: # Added encoding
        html_content = file.read()
    
    st.success(f"[DEBUG] File read successfully. Length: {len(html_content)}. First 50 chars: '{html_content[:50]}'")
    st.info("[DEBUG] Attempting components.html()...")
    
    components.html(html_content, height=800)
    
    st.success("[DEBUG] components.html() call completed.")

except FileNotFoundError as e:
    st.error(f"Error: HTML file not found. Primary attempt failed for path: {html_file_path_to_try}")
    st.error(f"Underlying error: {e}")
    st.error(f"Current Working Directory (os.getcwd()): {os.getcwd()}")
    
    st.error("--- Debugging Info ---")
    st.error(f"__file__ variable: {__file__}")
    st.error(f"os.path.abspath(__file__): {os.path.abspath(__file__)}")
    st.error(f"Script directory (calculated from __file__): {script_dir_file_based}")
    st.error(f"Path attempted based on __file__: {path_file_based}")
    st.error(f"Does __file__ based path exist? {os.path.exists(path_file_based)}")

    st.error(f"Path attempted relative to repo root: {path_relative_to_repo_root}")
    st.error(f"Does repo_root based path exist? {os.path.exists(path_relative_to_repo_root)}")

    # Check contents of expected static directories
    # Static dir based on __file__
    static_dir_file_based_check = os.path.join(script_dir_file_based, "static")
    st.error(f"Checking static directory (__file__ based): {static_dir_file_based_check}")
    if os.path.exists(static_dir_file_based_check) and os.path.isdir(static_dir_file_based_check):
        st.error(f"Contents of {static_dir_file_based_check}: {os.listdir(static_dir_file_based_check)}")
    else:
        st.error(f"Static directory (__file__ based) not found or not a directory: {static_dir_file_based_check}")

    # Static dir relative to repo root (assuming CWD is repo root)
    static_dir_repo_relative_check = os.path.join("Quantheo_Labs", "static") # Path from CWD
    st.error(f"Checking static directory (repo relative from CWD): {static_dir_repo_relative_check}")
    if os.path.exists(static_dir_repo_relative_check) and os.path.isdir(static_dir_repo_relative_check):
        st.error(f"Contents of {static_dir_repo_relative_check} (from CWD): {os.listdir(static_dir_repo_relative_check)}")
    else:
        st.error(f"Static directory (repo relative from CWD) not found or not a directory: {static_dir_repo_relative_check}")
        # If CWD is /mount/src/quantheo-labs, then this path is /mount/src/quantheo-labs/Quantheo_Labs/static
        # Let's also check one level up for static, in case CWD is Quantheo_Labs
        static_dir_one_level_up_check = os.path.join("..", "Quantheo_Labs", "static")
        if os.path.exists(static_dir_one_level_up_check) and os.path.isdir(static_dir_one_level_up_check):
             st.error(f"Alternative check: Contents of {static_dir_one_level_up_check}: {os.listdir(static_dir_one_level_up_check)}")


    # If the primary attempt (__file__ based) failed, try the repo_root relative one as a fallback
    st.error("Attempting fallback to path relative to repo root...")
    try:
        with open(path_relative_to_repo_root, "r", encoding="utf-8") as file: # Added encoding
            html_content_fallback = file.read()
        components.html(html_content_fallback, height=800)
        st.success("Fallback path worked!")
    except FileNotFoundError as e2:
        st.error(f"Fallback attempt also failed for path: {path_relative_to_repo_root}")
        st.error(f"Underlying error for fallback: {e2}")

except Exception as e_general: # New general exception handler
    st.error(f"!!! An unexpected error occurred AFTER successfully reading the file (or during components.html) !!!")
    st.error(f"Path attempted: {html_file_path_to_try}")
    st.error(f"Error type: {type(e_general).__name__}")
    st.error(f"Error details: {e_general}")
    st.error(f"Current Working Directory (os.getcwd()): {os.getcwd()}")
    st.error(f"__file__ variable: {__file__}")
    st.error(f"os.path.abspath(__file__): {os.path.abspath(__file__)}")
    st.error(f"Script directory (calculated from __file__): {script_dir_file_based}")
    if 'html_content' in locals() and html_content is not None:
        st.error(f"HTML content was read (length {len(html_content)}). First 100 chars: {html_content[:100]}")
    else:
        st.error("HTML content was NOT read or was None.")