# README - InvestAI

## Descriptif de l'Application

InvestAI est un projet révolutionnaire conçu pour outiller les investisseurs dans leurs décisions financières en utilisant une approche holistique et intelligente. En combinant le scraping de données en temps réel depuis des sources de confiance telles que Finviz et Yahoo Finance, l'analyse de données historiques, l'application de modèles de prédiction avancés, et l'évaluation du sentiment des actualités financières, InvestAI offre une perspective complète et captivante pour guider les investisseurs dans le monde complexe et dynamique du marché financier.

Pour plus de détails, nous vous invitons à consulter la page d'acceuil de l'application.

L'équipe InvestAI.

## Comment obtenir l'application?

Pour obtenir l'application, il n'y a rien de plus simple.
Notre équipe de développeurs a fait montre de son talent en déployant l'application sur le Hub de l'entreprise Docker (Docker Hub) de sorte qu'elle soit accessible à toute personne depuis n'importe quel endroit du globe et à tout moment.
En effet, le docker est hebergé sur l'addresse suivante : https://hub.docker.com/repository/docker/yohanamuah/investai/general

Depuis un terminal linux, il vous suffit de télécharger l'image docker en utilisant la commande suivante:
docker pull yohanamuah/investai .

Une fois, l'image téléchargée, il vous faut monter et créer le container de l'image, en utilsant la comande suivante:

docker run -p 9191:9191 yohanamuah/investai ./main_collector.sh <Ticker_de_l_action> <fréquence_des_donnees> <le_nombre_d_annees_de_donnees_a_telecharger>

## IMPORTANT !
<Ticker_de_l_action> : symbole utilisé pour décrire une action sur les marchés financiers

<fréquence_des_donnees> : la fréquence d'apparition des données (jour: 1d, semaine:1wk, mois:1mo, trimestre:3mo, année:1y)

<le_nombre_d_annees_de_donnees_a_telecharger> : l'horizon temporelle 

## Exemples

* AAPL pour le ticker d'Apple; TSLA pour le ticker de TESLA; ^GSPC pour le SP500; GOOGL pour GOOGLE; SBUX pour l'action Starbucks; etc.

* Il est aussi possible de scrapper les données de cryptomonnaies BTC-USD pour le bitcoin; ETH-USD pour l'Ethereum USD; etc.

* pour la fréquence, si vous voulez des données trimestrielles, vous mettrez "3mo"

* Et si vous voulez collecter ces données sur 200 ans , il faudrait ajouter "200y"

* Finalment, la commande:
  
  docker run -p 9191:9191 yohanamuah/investai ./main_collector.sh AAPL 3mo 100y
  
  servira à scraper les données  *trimestrielles* de l'action *APPLE* sur *100 années*.






