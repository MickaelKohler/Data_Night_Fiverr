import pandas as ps
import streamlit as st

st.markdown("""  <style> .reportview-container { background:
    url("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/image_fiverr2.png?raw=true")}
    </style> """, unsafe_allow_html=True)

st.sidebar.title('Hackathon Challenge')
st.sidebar.subheader('Navigation')

categorie = st.sidebar.radio("Categories", ("Home", "Data Cleaning","DataViz",
                                            "Maching Learning","NLP"))


if categorie == 'Home':
    st.markdown("***")
    st.title('Home')
    st.write("Context:")
    st.write("Tons of gigs are made every day, and so Fiverr's algorithm highlights certain seller profiles more than others. This is where rules could be established to support the freelancers community.")
    st.write("Problematic:")
    st.write("Your objective is to advise the Fiverr freelancers on how to fill efficiently their Seller Profile. To find, quantify and interpret the quality criteria. Use all the techniques you know, in particular NLP for text processing, and supervised or unsupervised machine learning.")

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
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/title_schema.png?raw=true")

