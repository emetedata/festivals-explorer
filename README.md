THE FILE CONTAINS:

- scraper_wegow_completo.py with the web scraping.
- limpieza_y_graficos.ipynb with the cleaning process and the generation of charts and maps using Plotly and Folium.
- appfunctions.py with the Streamlit app.
- mapa.html
- data folder with the data needed to run the project.
- images folder
- graphics folder

INSTRUCTIONS TO RUN THE PROJECT:

- To run scraper_wegow_completo.py, set the local directory and execute it; no extra packages are required.
- To run appfunctions.py, open the console, navigate to the project directory, and execute:
  streamlit run appfunctions.py
- appfunctions.py requires the external package lottie:
  pip install lottie

CONTENT OF THE PROJECT:

- Based on the scraped data from Wegow, the project extracts insights about the prices of different events considering additional factors such as the month, the city, or the music genre.
- Objective: Analyze music festivals in Spain: identify how many festivals exist, where they are located, and compare prices across events.
- What I did: Collected and cleaned festival data from multiple sources, and built interactive visualizations and a map in Streamlit.
