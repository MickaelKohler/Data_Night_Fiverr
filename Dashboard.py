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

categorie = st.sidebar.radio("Categories", ("The Mission", "Clustering", "Overview", 'Pricing', 'Description'))


# MAIN PAGE #
col1, col2 = st.beta_columns([2, 1])
with col2:
    st.image('https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/logo.png', width=250)
if categorie == 'The Mission':
    st.markdown("***")
    st.title('The Start')
    st.subheader("The Context")
    st.markdown(
        '''
        Tons of gigs are made every day, and so Fiverr's algorithm highlights certain seller profiles more than others. 
        This is where rules could be established to support the freelancers community.
        ''')

    st.subheader("The Mission")
    st.write(
        '''
        Your objective is to advise the Fiverr freelancers on how to fill efficiently their Seller Profile. 
        To find, quantify and interpret the quality criteria. Use all the techniques you know, 
        in particular NLP for text processing, and supervised or unsupervised machine learning.
        ''')

    st.subheader('The Data')
    st.write(
        '''
        The study is based on a database of 950 sellers on the Fiverr platform. Let’s see who are they.
        ''')
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

    fig = px.histogram(df, x="user-stats-member-since 1", nbins=16, color_discrete_sequence=['#1dbf73'],
                       title='<b>What is their seniority ?</b>')
    st.plotly_chart(fig, use_container_width=True)

if categorie == 'Clustering':
    st.markdown("***")
    st.title('Clustering')

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
        st.subheader(" ")
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
        st.plotly_chart(fig, use_container_width=True)
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/title_schema.png?raw=true")
    st.title('Add your metadata')
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/metadata1.png?raw=true")
    col1, col2 = st.beta_columns([5, 4])
    with col1:
        fig = go.Figure(go.Bar(
            y=[5.5, 8],
            x=['Cluster 1', 'Cluster 2'],
            marker_color=['lightgray', '#1dbf73'],
            text=[5.5, 8],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} fields')
        fig.update_layout(template='plotly_white', showlegend=False, font_family='IBM Plex Sans',
                          font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                          height=300)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader(" ")



if categorie == 'Pricing':
    st.markdown("***")
    st.title('Choose the best pricing')
    fig = go.Figure()
    fig.add_trace(go.Box(y=df[df['cluster']==1]['package1-price 1'], name='Cluster 1',
                    marker_color = 'lightgrey'))
    fig.add_trace(go.Box(y=df[df['cluster']==0]['package1-price 1'], name = 'Cluster 2',
                    marker_color = '#1dbf73'))
    fig.add_trace(go.Box(y=df[df['cluster']==1]['package2-price 1'], name = 'Cluster 1 ',
                    marker_color = 'lightgrey'))
    fig.add_trace(go.Box(y=df[df['cluster']==0]['package2-price 1'], name = 'Cluster 2 ',
                    marker_color = '#1dbf73'))
    fig.add_trace(go.Box(y=df[df['cluster']==1]['package3-price 1'], name='Cluster 1  ',
                    marker_color = 'lightgrey'))
    fig.add_trace(go.Box(y=df[df['cluster']==0]['package3-price 1'], name = 'Cluster 2  ',
                    marker_color = '#1dbf73'))
    fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
    fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor ='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor ='rgba(0,0,0,0)')
    fig.update_yaxes(title_text="<b>Prix", range = [0,1000])
    fig.update_layout(title_text="<b>Prices by clusters", title_x=0.5, title_font_family="Verdana")
    fig.add_annotation(
            x=2.5,
            y=1000,
            xref="x",
            yref="y",
            text="Prix 2",
            showarrow=False,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=20,
            ay=-30,
            bordercolor="#AED6F1",
            borderwidth=2,
            borderpad=2,
            bgcolor="#AED6F1",
            opacity=0.8
            )
    fig.add_annotation(
            x=0.5,
            y=1000,
            xref="x",
            yref="y",
            text="Prix 1",
            showarrow=False,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=20,
            ay=-30,
            bordercolor="#AED6F1",
            borderwidth=2,
            borderpad=2,
            bgcolor="#AED6F1",
            opacity=0.8
            )
    fig.add_annotation(
            x=4.5,
            y=1000,
            xref="x",
            yref="y",
            text="Prix 3",
            showarrow=False,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=20,
            ay=-30,
            bordercolor="#AED6F1",
            borderwidth=2,
            borderpad=2,
            bgcolor='#AED6F1',
            opacity=0.8
            )
    fig.update_layout(showlegend=False)


    st.write(fig)
    st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/blob/main/pricing1.png?raw=true")

if categorie == 'Description':
    st.markdown("***")
    st.title('Description')
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
    