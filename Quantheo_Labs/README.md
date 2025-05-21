# Quantheo Labs

Quantheo Labs is a Streamlit project that provides an interactive celestial simulation, showcasing a 3D solar system visualization using Three.js.

## Project Structure

```
Quantheo_Labs
├── app.py
├── static
│   └── celestial_simulation.html
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Quantheo_Labs
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run app.py
```

Once the application is running, open your web browser and navigate to `http://localhost:8501` to view the celestial simulation.

## Features

- Interactive 3D solar system visualization.
- Clickable planets to learn more about each celestial body.
- Responsive design for various screen sizes.

## Acknowledgments

This project utilizes Three.js for 3D rendering and Streamlit for creating the web application interface.