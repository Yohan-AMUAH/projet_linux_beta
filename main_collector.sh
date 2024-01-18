#!/bin/bash
echo "Vérifier si le nombre d'arguments est correct"
# Vérifier si le nombre d'arguments est correct
if [ "$#" -ne 3 ]; then
                    echo "Usage: $0 <ticker> <fréquence> <période>"
                                    exit 1
fi

echo "récupération des arguments"
# Récupérer les arguments
ticker="$1"
frequence="$2"
periode="$3"


# Scraper les données
chmod +x scraping_yahoo_finance_final.sh
./scraping_yahoo_finance_final.sh ${ticker} ${frequence} ${periode}





##########################################################################
chmod +x main_processor.py
python3 main_processor.py


sudo apt-get update
sudo apt-get install python3-pip
pip install -r requirements.txt


streamlit run App_streamlit_Linux_baseline.py --server.port 9191
