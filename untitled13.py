# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IygClG5BMoNZ1kcEG-9fuMENEDYmd099
"""
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt



st.sidebar.title("Pagina del apoyo para el juego Fortnite ")
st.sidebar.header("Saludos Gamer")
st.sidebar.write("Espero que te encuentres bien")

st.sidebar.image("OIP.jpg")


if st.sidebar.button("Haz click abajo"):
   st.sidebar.write("Más abajo")

                     
user_input= st.sidebar.text_input("Escribe tu usuario:")
st.sidebar.write("Saludos usuario, en esta pagina te daremos una pequeña ayuda para mejorar en este Videojuego")
st.sidebar.write("Espero que estos videos de apoyo te sirvan", user_input)

st.title("Mejora tu calidad de juego")
st.write("Para empezar a mejorar en este juego, necesitaremos una buena configuracion de construccion y edicion")
st.write("Aqui abajo te dejare un link para que conozca una de las mejores configuraciones de este juego")
st.write("Recuerda que estos videos son de apoyo y que la mejor configuracion siempre sera la que a ti te acomode")
link_video= "https://youtu.be/LMXX54rQ3Eo?si=Ag8yEGfE9KvftuwI"
st.video(link_video)

st.write("Ahora que sabemos que configuracion nos acomoda más, debemos conocer cuales armas tenemos esta temporada y conocerlas")
st.write("Abajo te dejare un link con el cual podras ver cuales son las nuevas armas, como se utilizan y que tan buenas son")
url_video="https://youtu.be/TLrOiFsoQe8?si=BUr7ECIIJy0XI6ek"
st.video(url_video)

