import pandas as ps
import streamlit as st

st.markdown("""  <style> .reportview-container { background:
    url("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/image_fiverr2.png?raw=true")}
    </style> """, unsafe_allow_html=True)

st.sidebar.title('Hackathon Challenge')
st.sidebar.subheader('Navigation')

categorie = st.sidebar.radio("Categories", ("Accueil", "Data Cleaning","DataViz",
                                            "Maching Learning","NLP"))


if categorie == 'Accueil':
    st.markdown("***")
    st.title('Accueil')

if categorie == 'Data Cleaning':
    st.markdown("***")
    st.title('Data Cleaning')

if categorie == 'DataViz':
    st.markdown("***")
    st.title('DataViz')

if categorie == 'Maching Learning':
    st.markdown("***")
    st.title('Maching Learning')

if categorie == 'NLP':
    st.markdown("***")
    st.title('NLP')

