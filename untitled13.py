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


st.sidebar.image()

if st.sidebar.button("Haz click abajo"):
   st.sidebar.write("Haz hecho click en el boton")

                     
user_input= st.sidebar.text_input("Escribe tu usuario:")
st.sidebar.write("Hola", user_input)
