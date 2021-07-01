import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Data Night Fiverr",
                   page_icon="🚀")

# FONCTION #


@st.cache
def load_data(url):
    return pd.read_csv(url)


# DATA #

DB_CLUSTURING = 'https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/Databases/data_clustured.csv'
DB_CLEAN = 'https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/Databases/db_clean.csv'
df = load_data(DB_CLUSTURING)
df_clean = load_data(DB_CLEAN)

# SIDEBAR #

st.sidebar.title('Hackathon Challenge :rocket:')
st.sidebar.subheader('Navigation')

categorie = st.sidebar.radio("Categories", ("The Mission", "The Data", "Clustering", "Optimize a seller profile"))

if categorie == 'Optimize a seller profile':
    sub_categorie = st.sidebar.radio("Optimize a seller profile", ('Overview',
                                                                   'Pricing',
                                                                   'Description'))
if categorie == 'Optimize a seller profile':
    for n in range(4):
        st.sidebar.title(' ')
else:
    for n in range(8):
        st.sidebar.title(' ')
st.sidebar.info('Made by the **Data Night Fiverr Team**: _Maxime, Michaël, Mickaël, Sebastien_')
st.sidebar.info('Hackathon organized by the **WildCodeSchool** in partnership with *Fiverr*, on 06/30/2021')

# MAIN PAGE #
col1, col2 = st.beta_columns([2, 1])
with col2:
    st.image('https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/Ressources/logo.png', width=250)
if categorie == 'The Mission':
    st.markdown("***")
    col1, col2, col3 = st.beta_columns([3, 2, 3])
    with col2:
        st.title('The Start')
        st.title(' ')
    st.subheader("The Context")
    st.markdown(
        '''
        Tons of gigs are made every day, and so Fiverr's algorithm highlights certain seller profiles more than others. 
        This is where rules could be established to support the freelancers community.
        ''')

    st.subheader("The Mission")
    st.write(
        '''
        The objective is to advise the Fiverr freelancers on how to fill efficiently their Seller Profile. 
        To find, quantify and interpret the quality criteria, all the techniques of NLP for text processing, 
        and supervised or unsupervised machine learning can be use.
        ''')

    st.subheader('The Data')
    st.write(
        '''
        The study is based on a **database of 951 sellers** of the Fiverr platform. *Let’s see who they are !*
        ''')

if categorie == 'The Data':
    st.markdown("***")
    col1, col2, col3 = st.beta_columns([2, 3, 2])
    with col2:
        st.title('The Dataset')
        st.title(' ')
    # country repartition
    countries = pd.DataFrame((df['user-stats-from 1'].value_counts(normalize=True)*100).round(2)).iloc[:10]
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
            colorscale='Tealgrn',
            colorbar=dict(
                title="Percent",
                ticksuffix=" %",
            ),
        )
    )])
    fig.update_layout(font_family='IBM Plex Sans',
                      title='<b>Which country do Fiverrs come from ?</b>',
                      uniformtext_minsize=14, uniformtext_mode='hide',
                      title_x=0.5, font_size=13,
                      margin=dict(l=10, r=10, b=10),
                      plot_bgcolor='rgba(0,0,0,0)',
                      )
    fig.update_yaxes(title=None, showticklabels=False)
    st.plotly_chart(fig, use_container_width=True)

    # age repartition
    fig = px.histogram(df_clean, x="user-stats-member-since 1", nbins=20, color_discrete_sequence=['#1dbf73'],
                       title='<b>What is their seniority ?</b>')
    fig.update_layout(title_x=0.5, font_size=13, template='plotly_white', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(title='Years of seniority')
    fig.update_yaxes(title='Numbers of Fiverrs')
    st.plotly_chart(fig, use_container_width=True)

    # level reparition
    pivot = df.pivot_table(values='Address', index='seller-level 1', aggfunc='count')
    pivot = pivot.sort_values('seller-level 1', ascending=False)
    pivot = pivot.reset_index()

    fig3 = px.pie(pivot, values='Address', names='seller-level 1', labels='seller-level 1',
                  color_discrete_sequence=px.colors.sequential.Tealgrn_r, hole=.5)
    fig3.update_layout(width=800, height=500, showlegend=False,
                       title="<b>What is their level ?</b>", font_size=13,
                       title_x=0.5, title_font_family="Verdana")
    fig3.update_traces(textposition='inside', texttemplate="<br>%{percent:%f}", textfont_size=15)
    fig3.update_yaxes(color='white')
    fig3.update_xaxes(color='white')
    fig3.add_annotation(
        x=5,
        y=1000,
        xref="x",
        yref="y",
        text="Level 2 Sellers",
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
        ax=20,
        ay=-30,
        borderwidth=2,
        borderpad=2,
        bgcolor='#257d98',
        opacity=0.8
    )
    fig3.add_annotation(
        x=4.8,
        y=990,
        xref="x",
        yref="y",
        text="Top Sellers",
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
        ax=20,
        ay=-30,
        borderwidth=2,
        borderpad=2,
        bgcolor='#4ac8a4',
        opacity=0.8
    )
    fig3.add_annotation(
        x=2,
        y=990,
        xref="x",
        yref="y",
        text="Level 1 Sellers",
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
        ax=20,
        ay=-30,
        borderwidth=2,
        borderpad=2,
        bgcolor='#38b2a3',
        opacity=0.8
    )
    fig3.add_annotation(
        x=2,
        y=1000,
        xref="x",
        yref="y",
        text='No Level',
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
        ax=20,
        ay=-30,
        borderwidth=2,
        borderpad=2,
        bgcolor='#2c98a1',
        opacity=0.8
    )
    fig3.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)', 'paper_bgcolor': 'rgba(0,0,0,0)'})
    st.plotly_chart(fig3, use_container_width=True)


if categorie == 'Clustering':
    st.markdown("***")
    col1, col2, col3 = st.beta_columns([3, 2, 3])
    with col2:
        st.title('Clustering')
        st.title(' ')

    st.subheader('Why looking for clusters of sellers ?')
    st.markdown('''
        Seller's level ? Number of rates ? Or, number of bookmarks ?...
        
        Any of these indicators can, by itself, explain what a good profile is.
        These indicators are strongly related to the seniority of the seller.   
    ''')

    data = df_clean.groupby('seller-level 1').mean()[['user-stats-member-since 1']]
    fig = go.Figure(go.Bar(
        x=['No Level', 'Level 1', 'Level 2', 'Top Rated'],
        y=data['user-stats-member-since 1'],
        marker={'color': ['#1dbf73']*4},
        text=data['user-stats-member-since 1'].round(2),
        textposition='auto'))
    fig.update_traces(texttemplate='%{text} years', textfont_size=15)
    fig.update_layout(showlegend=False, font_family='IBM Plex Sans',
                      font_size=13, margin=dict(l=20, r=10, b=0, t=60),
                      title="Sellers' seniority according to their level",
                      title_x=.5, height=350)
    fig.update_xaxes(title=None, dtick=1)
    st.plotly_chart(fig, use_container_width=True)

    data = df_clean.groupby('seller-level 1').median()[['ratings-count 1', 'collect-count 1']]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['No Level', 'Level 1', 'Level 2', 'Top Rated'],
                             y=data['ratings-count 1'],
                             line=dict(color='#257d98', width=4),
                             name='Number of rates'))
    fig.add_trace(go.Scatter(x=['No Level', 'Level 1', 'Level 2', 'Top Rated'],
                             y=data['collect-count 1'],
                             line=dict(color='#38b2a3', width=4),
                             name='Number of bookmarks'))
    fig.update_layout(font_family='IBM Plex Sans',
                      title=None,
                      margin=dict(l=10, r=10, b=80, t=0),
                      height=550,
                      hovermode="x",
                      font_size=13,
                      hoverdistance=100,
                      spikedistance=1000,
                      legend=dict(
                          orientation="h",
                          yanchor="bottom",
                          y=1.02,
                          xanchor="right",
                          x=1)
                      )
    fig.update_xaxes(dtick=1, title="Number of ratings and bookmarks according to the sellers' level",
                     linecolor="#BCCCDC",
                     showspikes=True,
                     spikethickness=2,
                     spikedash="dot",
                     spikecolor="#999999",
                     spikemode="across"
                     )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('So, how can we determine what is a good profile for a new registrant ?')

    st.markdown('***')

    st.subheader("The Selected Clusters' Characteristics")
    st.markdown("""
        A Machine Learning model was trained on the database and it identified 4 different types of sellers.
        
        We decided to compare *Custler 1* and *Cluster 2*.
    
        For the same number of scores approximately, **Cluster 2** has **less seniority**,
        but has **double the number of bookmakers**.""")

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        fig = go.Figure(go.Bar(
            y=[27, 31],
            x=['Cluster 1', 'Cluster 2'],
            marker={'color': ['lightgray', '#1dbf73']},
            text=[29, 33],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} rates')
        fig.update_layout(showlegend=False, font_family='IBM Plex Sans',
                          font_size=15, margin=dict(l=10, r=10, b=10, t=20), height=350)
        fig.update_xaxes(title='Number of ratings')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = go.Figure(go.Bar(
            y=[3.20, 2.3],
            x=['Cluster 1', 'Cluster 2'],
            marker={'color': ['lightgray', '#1dbf73']},
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
            marker={'color': ['lightgray', '#1dbf73']},
            text=[16, 29],
            textposition='auto'))
        fig.update_traces(texttemplate='%{text} add')
        fig.update_layout(showlegend=False, font_family='IBM Plex Sans',
                          font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                          height=350)
        fig.update_xaxes(title='Number of bookmarkes')
        st.plotly_chart(fig, use_container_width=True)

if categorie == 'Optimize a seller profile':
    if sub_categorie == 'Overview':
        st.markdown("***")
        col1, col2, col3 = st.beta_columns([1, 3, 1])
        with col2:
            st.title('Optimize a seller profile')
        col1, col2, col3 = st.beta_columns([2, 1, 2])
        with col2:
            st.subheader('Overview')
            st.title(' ')

        col1, col2 = st.beta_columns([5, 4])
        with col1:
            st.title(' ')
            st.subheader('How to create a title')
            st.title(' ')
            st.markdown('''
            The average length of a title is 50 characters. 
            Choose the words in the title well to have a good referencing. 
            ''')
        with col2:
            st.subheader(" ")
            fig = go.Figure(go.Bar(
                y=[52, 56],
                x=['Cluster 1', 'Cluster 2'],
                marker={'color': ['lightgray', '#1dbf73']},
                text=[52, 56],
                textposition='auto'))
            fig.update_traces(texttemplate='%{text} characters')
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', template='plotly_white', showlegend=False,
                              font_family='IBM Plex Sans', font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                              height=300)
            st.plotly_chart(fig, use_container_width=True)
        st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/Ressources/title.png")

        st.markdown('***')

        col1, col2, col3 = st.beta_columns([4, 3, 4])
        with col2:
            st.subheader('Add your metadata')
            st.title(' ')

        st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/Ressources/metadata1.png")
        col1, col2 = st.beta_columns([5, 4])
        with col1:
            fig = go.Figure(go.Bar(
                y=[5.5, 8],
                x=['Cluster 1', 'Cluster 2'],
                marker={'color': ['lightgray', '#1dbf73']},
                text=[5.5, 8],
                textposition='auto'))
            fig.update_traces(texttemplate='%{text} fields')
            fig.update_layout(template='plotly_white', plot_bgcolor='rgba(0,0,0,0)', showlegend=False, font_family='IBM Plex Sans',
                              font_size=15, margin=dict(l=10, r=10, b=10, t=20),
                              height=300)
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.title(' ')
            st.markdown("""
                Cluster 2 sellers add **47% more metadatas**.
                           
                Think to add as many as possible, it will improve the referencing !
             """)

    if sub_categorie == 'Pricing':
        st.markdown("***")
        col1, col2, col3 = st.beta_columns([1, 3, 1])
        with col2:
            st.title('Optimize a seller profile')
        col1, col2, col3 = st.beta_columns([3, 1, 3])
        with col2:
            st.subheader('Pricing')
            st.title(' ')

        fig = go.Figure()
        fig.add_trace(go.Box(y=df[df['cluster'] == 2]['package1-price 1'],
                             name='Cluster 1',
                             marker={'color': 'lightgrey'}))
        fig.add_trace(go.Box(y=df[df['cluster'] == 0]['package1-price 1'],
                             name='Cluster 2',
                             marker={'color': '#1dbf73'}))
        fig.add_trace(go.Box(y=df[df['cluster'] == 2]['package2-price 1'],
                             name='Cluster 1 ',
                             marker={'color': 'lightgrey'}))
        fig.add_trace(go.Box(y=df[df['cluster'] == 0]['package2-price 1'],
                             name='Cluster 2 ',
                             marker={'color': '#1dbf73'}))
        fig.add_trace(go.Box(y=df[df['cluster'] == 2]['package3-price 1'],
                             name='Cluster 1  ',
                             marker={'color': 'lightgrey'}))
        fig.add_trace(go.Box(y=df[df['cluster'] == 0]['package3-price 1'],
                             name='Cluster 2  ',
                             marker={'color': '#1dbf73'}))
        fig.update_layout(template='plotly_white', plot_bgcolor='rgba(0,0,0,0)')
        fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor='rgba(0,0,0,0)')
        fig.update_yaxes(title_text="<b>Price", range=[0, 1000])
        fig.update_layout(title_text="<b>Prices by clusters", title_x=0.5, title_font_family="Verdana",
                          margin=dict(l=10, r=10, b=40, t=60))
        fig.add_annotation(
                x=2.5,
                y=1000,
                xref="x",
                yref="y",
                text="Standard",
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
                text="Basic",
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
                text="Premium",
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
        st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/Ressources/pricing1.png")

    if sub_categorie == 'Description':
        st.markdown("***")
        col1, col2, col3 = st.beta_columns([1, 3, 1])
        with col2:
            st.title('Optimize a seller profile')
        col1, col2, col3 = st.beta_columns([2, 1, 2])
        with col2:
            st.subheader('Description')
            st.title(' ')

        fig = go.Figure()
        fig.add_trace(go.Box(y=df[df['cluster'] == 2]['len_description'],
                             name='Cluster 1',
                             marker={'color': 'lightgrey'}))
        fig.add_trace(go.Box(y=df[df['cluster'] == 0]['len_description'],
                             name='Cluster 2',
                             marker={'color': '#1dbf73'}))
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)', 'paper_bgcolor': 'rgba(0,0,0,0)'},
                          title_text="<b>Description's length by clusters", title_x=0.5,
                          title_font_family="Verdana", showlegend=False)
        fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor='rgba(0,0,0,0)')
        fig.update_yaxes(showgrid=False, gridwidth=1, gridcolor='white', linecolor='rgba(0,0,0,0)')
        st.plotly_chart(fig)
        st.image("https://github.com/MickaelKohler/Data_Night_Fiverr/raw/main/Ressources/description_1.png")
