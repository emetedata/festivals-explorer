THE FILE CONTAINS:

- scraper_wegow_completo.py with the web scraping.

- limpieza_y_graficos.ipynb with the cleaning process and the generation of charts and maps using Plotly and Folium.

- appfunctions.py with the Streamlit app.

- mapa.html

- data folder with the data needed to run the project.

- images folder

- graphics folder


INSTRUCTIONS TO RUN THE PROJECT:

- To run scraper_wegow_completo.py, you only need to set the local directory and execute it; no extra packages are required.

- To run appfunctions.py, open the console, navigate to the local directory and execute:
  streamlit run appfunctions.py

- To run appfunctions.py, an external package called lottie must be installed with:
  pip install lottie


CONTENT OF THE PROJECT:
- Based on the scraped data from Wegow, we extract insights about the prices of different events considering additional factors such as the month, the city, or the music genre.
