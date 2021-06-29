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
col1, col2 = st.beta_columns([2, 3])
with col2:
    st.image('https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/image_fiverr2.png?raw=true')
if categorie == 'Home':
    st.markdown("***")
    st.title('Home')
    st.write("Context:")
    st.write("Tons of gigs are made every day, and so Fiverr's algorithm highlights certain seller profiles more than others. This is where rules could be established to support the freelancers community.")
    st.write("Problematic:")
    st.write("Your objective is to advise the Fiverr freelancers on how to fill efficiently their Seller Profile. To find, quantify and interpret the quality criteria. Use all the techniques you know, in particular NLP for text processing, and supervised or unsupervised machine learning.")

if categorie == 'Clustering':
    st.markdown("***")
    st.title('Clustering')

    countries = pd.DataFrame((df['user-stats-from 1'].value_counts(normalize=True) * 100).round(2)).iloc[:10]
    fig = go.Figure(data=[go.Scatter(
        x=list(countries.index), y=[1] * 10,
        text=countries['user-stats-from 1'],
        mode='markers',
        marker=dict(
            size=countries['user-stats-from 1'],
            color=countries['user-stats-from 1'],
            sizemode='area',
            sizeref=0.002,
            showscale=True,
            colorscale='Tealgrn'
        )
    )])
    fig.update_layout(showlegend=False, font_family='IBM Plex Sans',
                      title='<b>Which country do Fiverrs come from ?</b>',
                      uniformtext_minsize=14, uniformtext_mode='hide',
                      margin=dict(l=10, r=10, b=10),
                      plot_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(title=None, showticklabels=False)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Why looking for clusters of sellers ?')

    fig = px.histogram(df, x="user-stats-member-since 1", nbins=16, color_discrete_sequence=['#1dbf73'])
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
        st.title(' ')
        st.markdown('''
        The average length of a title is 50 characters. Choose the words in the title well to have a good referencing. 
        ''')
    with col2:
        fig = go.Figure(go.Bar(
            y=[52, 56],
            x=['Cluster 1', 'Cluster 2'],
            marker_color=['lightgray', '#1dbf73'],
            text=[52, 56],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} characters')
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', template='plotly_white', showlegend=False,
                          font_family='IBM Plex Sans', font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                          height=300)
        fig.update_xaxes(title='Use the best lenght')
        st.plotly_chart(fig, use_container_width=True)
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/title_schema.png?raw=true")
    st.title('Add your metadata')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/metadata.png?raw=true")

if categorie == 'Pricing':
    st.markdown("***")
    st.title('Choose the best pricing')
    fig = go.Figure()
    
    # Defining y axis
    x = df['cluster']
    
    fig.add_trace(go.Box(
    
        # defining x axis in corresponding
        # to y-axis
        x=x,
        y=df['package1-price 1'],
        name='prix 1',
        marker_color='green'
    ))
    
    fig.add_trace(go.Box(
        x=x,
        y=df['package2-price 1'],
        name='prix 2',
        marker_color='yellow'
    ))
    
    fig.add_trace(go.Box(
        x=x,
        y=df['package3-price 1'],
        name='prix 3',
        marker_color='blue'
    ))
    
    fig.update_layout(
    
        # group together boxes of the different
        # traces for each value of y
        boxmode='group'
    )
    fig.update_xaxes(title_text="<b>Clusters", range = [-0.5,1.5])
    fig.update_yaxes(title_text="<b>Prix", range = [0,1000])
    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    fig.update_layout(title_text="<b>Répartition des prix par cluster", title_x=0.5, title_font_family="Verdana")


    
    # changing the orientation to horizontal
    # fig.update_traces(orientation='h')

    st.write(fig)
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/Pricing.png?raw=true")

if categorie == 'Description':
    st.markdown("***")
    st.title('... best description')
    st.title('')
    fig = go.Figure()
    fig.add_trace(go.Box(y=df[df['cluster']==2]['len_description'], name='Cluster 1',
                marker_color = 'lightgrey'))
    fig.add_trace(go.Box(y=df[df['cluster']==0]['len_description'], name = 'Cluster 2',
                marker_color = '#1dbf73'))
    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor ='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor ='rgba(0,0,0,0)')
    fig.update_layout(title_text="<b>Description's length by clusters", title_x=0.5, title_font_family="Verdana")
    fig.update_layout(showlegend=False)
    st.write(fig)
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/description_1.png?raw=true")
    