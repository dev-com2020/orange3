FROM nginx:1.21.6 
# Użyj obrazu bazowego nginx:1.21.6 z Docker Hub
# Dobra praktyka: zawsze używaj konkretnej wersji, :latest to ZŁO.

LABEL maintainer="Damian Naprawa <damian@szkoladockera.pl>"
# Ustaw etykietę maintainer

RUN apt-get update && apt-get install --no-install-recommends -y procps=3.2.8 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir /usr/moj/katalog
# Uruchom dowolne polecenie, które jest możliwe w obrazie bazowym

# Podczas budowania obraz:
COPY index.html docker.png /usr/share/nginx/html/
# Skopiuj lokalne pliki index.html i docker.png do /usr/share/nginx/html

EXPOSE 80 443 	
# UWAGA: To tylko informacja w metadanych obrazu (np. od programisty dla admina)
# Powyższe NIE powoduje udostępnienia portów w kontenerze po uruchomieniu

CMD ["nginx", "-g", "daemon off;"]
# Polecenie jakie ma zostać wykonane przy starcie kontenera
# Można je nadpisać `docker run dnaprawa/dwg-web:1.0 /bin/bash -c "sleep 20"`
