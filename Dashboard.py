import pandas as ps
import streamlit as st


st.sidebar.title('Hackathon Challenge')
st.sidebar.subheader('Navigation')

categorie = st.sidebar.radio("Categories", ("Accueil", "Data Cleaning","DataViz"
                                            "Maching Learning","NLP"))


if categorie == 'Accueil':
    st.title('Accueil')

if categorie == 'Data Cleaning':
    st.title('Data Cleaning')

if categorie == 'DataViz':
    st.title('DataViz')

if categorie == 'Maching Learning':
    st.title('Maching Learning')

if categorie == 'NLP':
    st.title('NLP')




# test

# let's code

# salut, beaucoup de travail nous attend jusqu'a demain

