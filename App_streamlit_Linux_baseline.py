# Importation des librairies necesaires

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
import subprocess
import hydralit_components as hc
import os
st.set_page_config(
page_title="InvestAI - SAD",
page_icon="\\home_page.gif",
layout="wide",
initial_sidebar_state="collapsed",
)

st.markdown("<h1 style='text-align: center; background-color: #000045; color: #ece5f6'>Invest AI - SAD</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; background-color: #000045; color: #ece5f6'>Un Système d'Aide à la Décision pour l'Investissement Financier Intelligent</h4>", unsafe_allow_html=True)




menu_data = [

    {'label':"Price Data"},
]

over_theme = {'txc_inactive': '#16284C'}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    #login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )

if menu_id == "Home":



    # Définir des couleurs attrayantes
    couleur_principale = "#3498db"  # Bleu
    couleur_secondaire = "#2ecc71"  # Vert

    # Définir le style de page
    st.markdown(
        f"""
        <style>
            .reportview-container {{
                background: {couleur_principale};
                color: white;
            }}
            .sidebar .sidebar-content {{
                background: {couleur_principale};
            }}
            .Widget {{
                color: {couleur_principale};
                background-color: #ecf0f1;
            }}
            .stButton > button {{
                color: white;
                background-color: {couleur_secondaire};
            }}
            .stTextInput > div > div > input {{
                color: {couleur_principale};
                background-color: #ecf0f1;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Titre de la page
    st.title("InvestAI - Révolutionnez vos décisions financières")

    # Afficher le GIF avec la fonction st.image
    st.image("home_page.gif", use_column_width=False, width=1200)

    # Introduction
    st.write("""
    InvestAI est un projet révolutionnaire conçu pour outiller les investisseurs dans leurs décisions financières en utilisant une approche holistique et intelligente. En combinant le scraping de données en temps réel depuis des sources de confiance telles que Finviz et Yahoo Finance, l'analyse de données historiques, l'application de modèles de prédiction avancés, et l'évaluation du sentiment des actualités financières, InvestAI offre une perspective complète et captivante pour guider les investisseurs dans le monde complexe et dynamique du marché financier.
    """)

    # Fonctionnalités Clés
    st.header("Fonctionnalités Clés")

    # Scraping de Données en Temps Réel
    st.subheader("Scraping de Données en Temps Réel")
    st.write("InvestAI extrait des données financières en temps réel à partir de deux sources majeures : Finviz et Yahoo Finance. Cette collecte en temps réel assure des informations à jour et pertinentes pour une prise de décision informée.")

    # Modèles de Prédiction Avancés
    st.subheader("Modèles de Prédiction Avancés")
    st.write("Le projet intègre des modèles de prédiction sophistiqués basés sur l'apprentissage automatique pour anticiper les tendances du marché. Ces modèles utilisent des indicateurs techniques tels que MACD, RSI, ADX, et les bandes de Bollinger pour fournir des prédictions précises.")

    # Analyse de Sentiment
    st.subheader("Analyse de Sentiment")
    st.write("InvestAI analyse le sentiment des actualités financières en extrayant des informations pertinentes à partir des publications de sites de confiance. Cette analyse aide les investisseurs à comprendre le climat émotionnel entourant un actif particulier.")

    # Interface Conviviale
    st.subheader("Interface Conviviale")
    st.write("Une interface conviviale offre aux utilisateurs une expérience transparente pour explorer les données, visualiser les tendances, et obtenir des recommandations basées sur des paramètres spécifiques.")

    # Avantages pour les Investisseurs
    st.header("Avantages pour les Investisseurs")

    # Décisions Éclairées
    st.subheader("Décisions Éclairées")
    st.write("InvestAI fournit des données en temps réel et des analyses approfondies, permettant aux investisseurs de prendre des décisions éclairées.")

    # Réduction des Risques
    st.subheader("Réduction des Risques")
    st.write("Les modèles de prédiction et l'analyse de sentiment contribuent à minimiser les risques en anticipant les fluctuations du marché et en identifiant les signaux potentiels.")

    # Personnalisation
    st.subheader("Personnalisation")
    st.write("Les investisseurs peuvent personnaliser leurs préférences, intégrant des stratégies d'investissement spécifiques et ajustant les paramètres des modèles selon leurs besoins.")

    # Veille Concurrentielle
    st.subheader("Veille Concurrentielle")
    st.write("InvestAI fournit un avantage concurrentiel en surveillant constamment les changements sur les marchés et en informant les investisseurs sur les opportunités émergentes.")

    # Conclusion
    st.write("""
    En résumé, InvestAI transforme la manière dont les investisseurs abordent le marché financier, en alliant la puissance des données en temps réel, de l'analyse prédictive et du sentiment des actualités pour créer une approche complète, intelligente, et avant-gardiste de la prise de décision en matière d'investissement.
    """)






if menu_id == "Price Data":

    #definition des sidebars
    st.title("Stock Price Predictor")

    # Message d'astuce de navigation
    message_astuce = """
    **Sujet : Important - Astuce de Navigation dans l'Application InvestAI**

    Cher utilisateur d'InvestAI,

    Nous espérons que votre expérience sur notre plateforme est aussi enrichissante que possible. Pour vous assurer de tirer le meilleur parti de notre application, nous aimerions partager avec vous une astuce de navigation qui pourrait vous échapper.

    👉 **Astuce de Navigation :**

    L'onglet de navigation essentiel se trouve discrètement sur le bord gauche de la page. Assurez-vous de déplier cet onglet pour accéder à une panoplie de fonctionnalités exclusives, de visualisations détaillées, et de puissants outils d'analyse. C'est votre passerelle vers une expérience utilisateur complète et personnalisée !

    N'oubliez pas de jeter un coup d'œil et de débloquer le plein potentiel d'InvestAI.

    Pour toute question ou assistance, n'hésitez pas à nous contacter. Bonne exploration !

    Bien Cordialement,

    L'équipe InvestAI

    """



    # Afficher le message d'astuce dans Streamlit
    st.markdown(message_astuce)

    #ticker = st.sidebar.text_input('Ticker')
    #start_date = st.sidebar.date_input('Start Date')
    #end_date = st.sidebar.date_input('End Date')
    #frequency = st.sidebar.selectbox('Veullez selectionner la fréquence que vous souhaitez avoir dans les données dans la liste qui vous ait proposée.', ["Daily","Weekly","Monthly","Quarterly"])
    #st.session_state.variable_section1=ticker
    #validation=st.sidebar.button("Valider")
    #if validation:
        #if frequency =="Daily":
            #frequency="1d"
        #elif frequency =="Weekly":
            #frequency ="1wk"
        #elif frequency =="Monthly":
            #frequency ="1mo"
        #elif frequency =="Quarterly":
            #frequency ="3mo"
        #st.write("vous avez validé")
        #inf={
            #"ticker":[ticker],
            #"start_date":[start_date],
            #"end_date": [end_date],
            #"frequency": [frequency]
        #}


        #st.write("vous avez choisi une plage qui va de:", start_date ,"à", end_date,"." )
        #subprocess.run(["python", "Scraping_Yahoo_f.py"], check=True)

        #import Scraping_Yahoo_finance , Scraping_Yahoo_f
        #Scraping_Yahoo_finance.syf(ticker,frequency,start_date,end_date)
        #Scraping_Yahoo_f.syf(ticker,frequency,start_date,end_date)

    #Chargement du fichier des données

    importer=st.button("Visualiser les résultats")

    if importer:
        data = pd.read_csv("historical_data.csv")
        st.dataframe(data)



        # plot de la figure qui retrace l'historisque
        fig = px.line(data, x=data.index, y=data["Adj Close"])
        st.plotly_chart(fig)



        st.header('Price Movement Informations')
        data2=data
        data2['variation']=data["Adj Close"]/data["Adj Close"].shift(1) - 1
        data2.dropna(inplace=True)
        st.write(data2[["Adj Close","variation"]])

        #partie data processor
        #from main_processor import processor
        #[annual_return,standard_deviation]=processor()
        resultats = pd.read_csv("resultats.csv")
        st.dataframe(resultats)

        st.write("the annual return of this action is", resultats["annual_return"][0] , "%")
        st.write("The Standard deviation of this action is", resultats["standard_deviation"][0], "%")

    else:
        st.write("vous devez cliquer sur le boutton Visualiser les résultats pour accéder aux résultats")
