import pandas as ps
import streamlit as st


st.sidebar.title('Hackathon Challenge')
st.sidebar.subheader('Navigation')

categorie = st.sidebar.radio("Categories", ("Home", "Clustering", "Overview", 'Pricing', 'Description'))


if categorie == 'Home':
    st.markdown("""  <style> .reportview-container { background:
    url("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/image_fiverr2.png?raw=true")}
    </style> """, unsafe_allow_html=True)
    st.markdown("***")
    st.title('Home')
    st.write("Context:")
    st.write("Tons of gigs are made every day, and so Fiverr's algorithm highlights certain seller profiles more than others. This is where rules could be established to support the freelancers community.")
    st.write("Problematic:")
    st.write("Your objective is to advise the Fiverr freelancers on how to fill efficiently their Seller Profile. To find, quantify and interpret the quality criteria. Use all the techniques you know, in particular NLP for text processing, and supervised or unsupervised machine learning.")

if categorie == 'Clustering':
    st.markdown("***")
    st.title('Clustering')

if categorie == 'Overview':
    st.markdown("***")
    st.title('How to create a title')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/title_schema1.png?raw=true")
    st.title('Add your metadata')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/metadata.png?raw=true")

if categorie == 'Pricing':
    st.markdown("***")
    st.title('Choose the best pricing')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/Pricing.png?raw=true")

if categorie == 'Description':
    st.markdown("***")
    st.title('... best description')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/Description.png?raw=true")
    