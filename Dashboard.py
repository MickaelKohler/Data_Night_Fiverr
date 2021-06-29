import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# FONCTION #

@st.cache
def load_data(url):
    return pd.read_csv(url)


# DATA #

DB_CLUSTURING = 'https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/db_clustering.csv'
df = load_data(DB_CLUSTURING)

# SIDEBAR #

st.sidebar.title('Hackathon Challenge')
st.sidebar.subheader('Navigation')

categorie = st.sidebar.radio("Categories", ("Home", "Clustering", "Overview", 'Pricing', 'Description'))


# MAIN PAGE #

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

    st.subheader('Why looking for clusters of sellers ?')

    fig = px.histogram(df, x="user-stats-member-since 1", nbins=16)
    st.plotly_chart(fig, use_container_width=True)




    st.subheader("The Selected Clusters' Characteristics")
    st.markdown("""For the same number of scores or so, cluster 2 has less seniority,
                but has double the number of bookmakers.""")

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        fig = go.Figure(go.Bar(
            y=[27, 31],
            x=['Cluster 1', 'Cluster 2'],
            marker_color=['lightgray', '#1dbf73'],
            text=[27, 31],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} rates')
        fig.update_layout(showlegend=False, font_family='IBM Plex Sans',
                          font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                          height=350)
        fig.update_xaxes(title='Number of ratings')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = go.Figure(go.Bar(
            y=[3.20, 2.3],
            x=['Cluster 1', 'Cluster 2'],
            marker_color=['lightgray', '#1dbf73'],
            text=[3.20, 2.3],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} years')
        fig.update_layout(showlegend=False, font_family='IBM Plex Sans',
                          font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                          height=350)
        fig.update_xaxes(title='Years since registration')
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        fig = go.Figure(go.Bar(
            y=[16, 29],
            x=['Cluster 1', 'Cluster 2'],
            marker_color=['lightgray', '#1dbf73'],
            text=[16, 29],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} add')
        fig.update_layout(showlegend=False, font_family='IBM Plex Sans',
                          font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                          height=350)
        fig.update_xaxes(title='Number of bookmarkes')
        st.plotly_chart(fig, use_container_width=True)

if categorie == 'Overview':
    st.markdown("***")
    col1, col2 = st.beta_columns([5, 4])
    with col1:
        st.title('How to create a title')
    with col2:
        fig = go.Figure(go.Bar(
            y=[52, 56],
            x=['Cluster 1', 'Cluster 2'],
            marker_color=['lightgray', '#1dbf73'],
            text=[52, 56],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} characters')
        fig.update_layout(template='plotly_white', showlegend=False, font_family='IBM Plex Sans',
                          font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                          height=300)
        fig.update_xaxes(title='Use the best lenght')
        st.plotly_chart(fig, use_container_width=True)
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/title_schema.png?raw=true")
    st.title('Add your metadata')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/metadata.png?raw=true")

if categorie == 'Pricing':
    st.markdown("***")
    st.title('Choose the best pricing')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/Pricing.png?raw=true")

if categorie == 'Description':
    st.markdown("***")
    st.title('... best description')
    st.title('')
    fig = go.Figure()
    fig.add_trace(go.Box(y=df[df['cluster']==1]['len_description'], name='Cluster 1',
                marker_color = 'lightgrey'))
    fig.add_trace(go.Box(y=df[df['cluster']==0]['len_description'], name = 'Cluster 2',
                marker_color = '#1dbf73'))
    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor ='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor ='rgba(0,0,0,0)')
    fig.update_layout(title_text="<b>Description's length by clusters", title_x=0.5, title_font_family="Verdana")
    fig.update_layout(showlegend=False)
    st.write(fig)
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/Description_1.png?raw=true")
    