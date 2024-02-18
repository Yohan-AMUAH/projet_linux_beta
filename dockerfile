FROM ubuntu:22.04

RUN apt update && apt-get install -y curl && apt-get install -y python3 && apt-get install -y python3-pip
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt

# Rendez le port 9191 accessible au monde extérieur à ce conteneur
EXPOSE 9191

# Définissez la variable d'environnement
ENV NAME World

CMD bash -c ". main_collector.sh"
