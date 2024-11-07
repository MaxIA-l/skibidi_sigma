# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IygClG5BMoNZ1kcEG-9fuMENEDYmd099
"""
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt


st.sidebar.title("Pagina del fornai og ")
st.sidebar.header("Hola Gamer")
st.sidebar.write("Espero que te encuentres bien")

st.sidebar.image("OIP.jpg")


if st.sidebar.button("Haz click abajo"):
   st.sidebar.write("Haz hecho click en el boton")

                     
user_input= st.sidebar.text_input("Escribe tu usuario:")
st.sidebar.write("Hola", user_input)

st.title("Mejora tu calidad de juego")
st.write("Para empezar a mejorar en este juego, necesitaremos una buena configuracion de construccion y edicion")
st.write("Aqui abajo te dejare un link para que conozca una de las mejores configuraciones de este juego")
st.write("Recuerda que estos videos son de apoyo y que la mejor configuracion siempre sera la que a ti te acomode")
link_video= "https://youtu.be/LMXX54rQ3Eo?si=Ag8yEGfE9KvftuwI"
st.video(link_video)
