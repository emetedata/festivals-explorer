import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json
import os


from streamlit.components.v1 import html

from streamlit_lottie import st_lottie

#abrimos los csv

data_path = "data"

festivales_city_clean = pd.read_csv(
    os.path.join(data_path, "festivales_city_clean.csv"), sep=',').drop_duplicates()

festivales_genre_clean = pd.read_csv(
    os.path.join(data_path, "festivales_genre_clean.csv"), sep=',').drop_duplicates()

festivales_concat = pd.read_csv(
    os.path.join(data_path, "festivales_concat.csv"), sep=',').drop_duplicates()

festivales_join = pd.read_csv(
    os.path.join(data_path, "festivales_join.csv"), sep=',').drop_duplicates()


numbers_to_months = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

# Leer mapa.html en la misma carpeta del script
script_dir = os.path.dirname(__file__)  # Directorio donde está este archivo .py
mapa_path = os.path.join(script_dir, "mapa.html")

with open(mapa_path, "r", encoding="utf-8") as f:
    mapa_html = f.read()


#Definimos una función para aplicar los estilos

def apply_custom_styles(
    font="poppins",
    background_color="#d7effa", 
    text_color="#000000",
    primary_color="#5c9fd9", 
    button_text_color="#ffffff",
    button_active_color="#3d7aa5", 
    button_active_text_color="#ffffff",
    secondary_background_color="#c9e4f4",
    accent_color="#000000",
    link_color="#4da8d9",
):
    st.markdown(
        f"""
        <style>
        /* Definir la fuente de la página */
        @import url('https://fonts.googleapis.com/css2?family={font}&display=swap');

        body {{
            background-color: {background_color};
            color: {text_color};
            font-family: '{font}', sans-serif;
        }}

        /* Personalizar los botones */
        .stButton>button {{
            background-color: {primary_color};
            color: {button_text_color};
            border: none;
            border-radius: 5px;
            font-weight: bold;
            padding: 10px;
            transition: background-color 0.3s ease;
        }}

        /* Cambiar el color del botón cuando se hace clic o está seleccionado */
        .stButton>button:active,
        .stButton>button:focus {{
            background-color: {button_active_color};  
            color: {button_active_text_color};  
        }}

        /* Personalizar el sidebar */
        .css-1d391kg {{
            background-color: {secondary_background_color};  
        }}

        .stApp {{
            background-color: {background_color};
        }}

        a {{
            color: {link_color};  
        }}

        .stTextInput, .stTextArea, .stMarkdown {{
            color: {accent_color};  
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Definimos una función para crear tarjetas personalizadas

def create_event_card(event_name, event_date, event_price, event_followers):
    tarjeta_html = f"""
    <div style="border: 3px solid #5c9fd9; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #ffe8db;">
        <h4 style="text-align: center; color: #2a5487; font-size: 16px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{event_name}</h4>
        <p style="font-size: 16px;"><strong>Date:</strong> {event_date}</p>
        <p style="font-size: 16px;"><strong>Price:</strong> {event_price}</p>
        <p style="font-size: 16px;"><strong>Followers on Wegow:</strong> {event_followers}</p>
    </div>
    """
    st.markdown(tarjeta_html, unsafe_allow_html=True)



# Definimos una función para abrir menus de columna

def column_menu(festivales, column):
    column_elements = festivales[column].unique()
    
    col1, col2 = st.columns([1, 1])

    with col1:
        radio_menu_option = st.radio(
            "Select an option",
            column_elements,
            label_visibility="collapsed")
    
    with col2:
        if column =='city' and len(column_elements)==11:
            st.image("images/sunsets2.jpg", use_container_width=True)
            
        if column =='genre':
            st.image("images/Concert_aesthetic.jpg",use_container_width=True)
            
        if column =='city' and len(column_elements)!=11:
            st.write("\n")
            st.write('Explore the data by city by hovering over the chart.')
            
        if column =='month_name':
            st.write("\n")
            st.write('Explore the data by month by hovering over the chart.')
            

    return radio_menu_option


#Definimos una función para mostrar los eventos
                        
def show_events(festivales, column, selection):
    events = festivales[festivales[column] == selection].drop_duplicates(subset=['event_names'])

    cols = st.columns(3)
    
    for idx, row in events.iterrows():
        event = row['event_names']
        
        with cols[idx % 3]:
            if st.button(f"{event}"):
                st.markdown("##### Event details:")
                
                create_event_card(
                    event_name=row['event_names'],
                    event_date=row['event_dates'],
                    event_price=row['event_prices'],
                    event_followers=row['event_followers'])


#Aplicamos el estilo

apply_custom_styles(
    font="poppins",
    background_color="#e0f5ff",
    text_color="#000000",
    primary_color="#5c9fd9",
    button_text_color="#ffffff",
    button_active_color="#3d7aa5",
    button_active_text_color="#ffffff",
    secondary_background_color="#c9e4f4",
    accent_color="#000000",
    link_color="#4da8d9",
)


#Menu de opciones lateral
side_menu_option = st.sidebar.selectbox("Choose an option:", ["Home","Festivals by city", "Festivals by genre","Compare prices" ,"Exit"])


if side_menu_option == "Home":
    st.title("Find Your Favorite Festival!")
    
    with open("images/animation.json", "r") as f:
        animation = json.load(f)
        
    col_animation, col_animation2, col_animation3 = st.columns([1, 2, 1])

    with col_animation2:

        st_lottie(animation, width=300, height=300,speed=1, loop=True)
    
    st.write("Discover and compare!")

    if st.button("Show map"):
        html(mapa_html, height=600)
        
        
if side_menu_option == "Festivals by city":
    st.title("Festivals by city")
    st.write("Select a city:")
    selected_city = column_menu(festivales_concat,'city')
    show_events(festivales_concat,'city', selected_city)
    
    
if side_menu_option == "Festivals by genre":
    st.title("Festivals by genre")
    st.write("Select a genre:")
    selected_genre = column_menu(festivales_genre_clean, 'genre')
    show_events(festivales_genre_clean, 'genre', selected_genre)
    

if side_menu_option == "Compare prices":
    st.title("Compare prices")
    selected_option = st.selectbox("How do you want to compare?", ['Compare by month','Compare by city']) 
    
    if selected_option =='Compare by month':
        festivales_join_sorted = festivales_join.sort_values('month')
        months = festivales_join.sort_values('month')
        festivales_join_sorted['month_name'] = festivales_join_sorted['month'].map(numbers_to_months)
        selected_month = column_menu(festivales_join_sorted, 'month_name')
        
        with open(f"graphics/grafico_{selected_month}.html", "r", encoding="utf-8") as f:
            graphic_month = f.read()
            html(graphic_month, height=600)
            
        if st.button('See general comparison'):
            with open("graphics/grafico_media_mes.html", "r", encoding="utf-8") as f:
                graphic_month = f.read()
                html(graphic_month, height=600)
            
    if selected_option =='Compare by city':
        festivales_concat_graf = festivales_concat[festivales_concat.event_prices != 'No se especifica']
        cities = festivales_concat_graf.city.unique()
        selected_city = column_menu(festivales_concat_graf, 'city')
        
        with open(f"graphics/grafico_{selected_city}.html", "r", encoding="utf-8") as f:
            graphic_month = f.read()
            html(graphic_month, height=600)
            
            if st.button('See general comparison'):
                with open("graphics/grafico_media_ciudad.html", "r", encoding="utf-8") as f:
                    graphic_month = f.read()
                    html(graphic_month, height=600)
             
            
if  side_menu_option == "Exit":
    st.write('See you soon! 🎶')
    with open("images/disc.json", "r") as f:
        disc = json.load(f)
        st_lottie(disc,speed=1, loop=True)
